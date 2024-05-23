# Copyright (c) 2021, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
import pickle
import pathlib
import tensorflow as tf

from nvflare.apis.event_type import EventType
from nvflare.apis.fl_constant import FLContextKey
from nvflare.apis.fl_context import FLContext
from nvflare.app_common.abstract.model import ModelLearnable
from nvflare.app_common.abstract.model import make_model_learnable
from nvflare.app_common.abstract.model_persistor import ModelPersistor
from nvflare.app_common.app_constant import AppConstants
import nvflare.app_common.shareablegenerators.full_model_shareable_generator as SG
import numpy as np
from oasysnow.nvflare.model.global_model import GlobalModel


class ModelRunner(ModelPersistor):
    def __init__(self, save_name="tf2_model.pkl"):
        super().__init__()
        self.save_name = save_name
        self.inputsize = 100
        self.model = None
        self.path_to_file = None

    def _initialize(self, fl_ctx: FLContext):
        # get save path from FLContext

        scope_properties = fl_ctx.get_prop(FLContextKey.SCOPE_PROPERTIES)
        print(">>>>>>>>>SCOPE", "SERVER", scope_properties)

        app_root = fl_ctx.get_prop(FLContextKey.APP_ROOT)
        env = None
        run_args = fl_ctx.get_prop(FLContextKey.ARGS)
        if run_args:
            env_config_file_name = os.path.join(app_root, run_args.env)
            if os.path.exists(env_config_file_name):
                try:
                    with open(env_config_file_name) as file:
                        env = json.load(file)
                except:
                    self.system_panic(
                        reason="error opening env config file {}".format(env_config_file_name), fl_ctx=fl_ctx
                    )
                    return

        if env is not None:
            if env.get("APP_CKPT_DIR", None):
                fl_ctx.set_prop(AppConstants.LOG_DIR, env["APP_CKPT_DIR"], private=True, sticky=True)
            if env.get("APP_CKPT") is not None:
                fl_ctx.set_prop(
                    AppConstants.CKPT_PRELOAD_PATH,
                    env["APP_CKPT"],
                    private=True,
                    sticky=True,
                )

        self.path_to_file = pathlib.Path(__file__).parent.resolve()
        log_dir = fl_ctx.get_prop(AppConstants.LOG_DIR)
        if log_dir:
            self.log_dir = os.path.join(app_root, log_dir)
        else:
            self.log_dir = app_root
        self._pkl_save_path = os.path.join(self.log_dir, self.save_name)
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        fl_ctx.sync_sticky()

        self.model = GlobalModel().get_model()
        self.xval = np.load(scope_properties['xtest'])
        self.yval = np.load(scope_properties['ytest'])

    def load_model(self, fl_ctx: FLContext) -> ModelLearnable:
        """
            initialize and load the Model.

        Args:
            fl_ctx: FLContext

        Returns:
            Model object
        """
        run_number = fl_ctx.get_job_id()
        client_name = fl_ctx.get_identity_name()

        print(">>>>>load_model", client_name, run_number)


        if os.path.exists(self._pkl_save_path):
            self.logger.info(f"Loading server weights")
            with open(self._pkl_save_path, "rb") as f:
                model_learnable = pickle.load(f)
        else:
            self.logger.info(f"Initializing server model")
            network = GlobalModel().get_model()
            loss_fn = tf.keras.losses.BinaryCrossentropy()
            network.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
            _ = network(tf.keras.Input(shape=100))
            var_dict = {str(key): value for key, value in enumerate(network.get_weights())}
            model_learnable = make_model_learnable(var_dict, dict())
        return model_learnable

    def handle_event(self, event: str, fl_ctx: FLContext):
        if event == EventType.START_RUN:
            self._initialize(fl_ctx)

    def save_model(self, model_learnable: ModelLearnable, fl_ctx: FLContext):
        """
            persist the Model object

        Args:
            model: Model object
            fl_ctx: FLContext
        """
        dxo = SG.model_learnable_to_dxo(model_learnable)
        weights = list(dxo.data.values())
        self.model.set_weights(weights)
        eval_result = self.model.evaluate(self.xval, self.yval)
        dict_result = dict(zip(self.model.metrics_names, eval_result))
        print(">>>>>>>> Analysis over the test set. SERVER", dict_result)

        model_learnable_info = {k: str(type(v)) for k, v in model_learnable.items()}
        self.logger.info(f"Saving aggregated server weights: \n {model_learnable_info}\n {self._pkl_save_path}")
        with open(self._pkl_save_path, "wb") as f:
            pickle.dump(model_learnable, f)
