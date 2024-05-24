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

import tensorflow as tf
from gennet.utils.LocallyDirected1D import LocallyDirected1D
from gennet.utils.Utility_functions import sensitivity, specificity
import scipy

class GenNet(tf.keras.Model):
    def __init__(self, genemask_path):
        super(GenNet, self).__init__()

        genemask = scipy.sparse.load_npz(genemask_path)
        self.inputsize = genemask.shape[0]
        self.reshape = tf.keras.layers.Reshape(input_shape=(self.inputsize,), target_shape=(self.inputsize, 1))
        self.gene_layer = LocallyDirected1D(mask=genemask,
                                            filters=1,
                                            input_shape=(self.inputsize, 1),
                                            kernel_regularizer=tf.keras.regularizers.l1(0.00001),
                                            activity_regularizer=tf.keras.regularizers.l1(1e-8),
                                            name="gene_layer")
        self.flatten = tf.keras.layers.Flatten()
        self.activation_tanh = tf.keras.layers.Activation("tanh")
        self.batchnorm = tf.keras.layers.BatchNormalization(center=False, scale=False, name="batchnorm_layer")
        self.output_node = tf.keras.layers.Dense(units=1,
                                                 kernel_regularizer=tf.keras.regularizers.l1(0.01),
                                                 activity_regularizer=tf.keras.regularizers.l1(1e-5),
                                                 activation="sigmoid",
                                                 name="dense_layer")

        self.sharable_layers = ['gene_layer', 'batchnorm_layer', 'dense_layer']


    def call(self, x):
        x = self.reshape(x)
        x = self.gene_layer(x)
        x = self.flatten(x)
        x = self.activation_tanh(x)
        x = self.batchnorm(x)
        x = self.output_node(x)
        return x

