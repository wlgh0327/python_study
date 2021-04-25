import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import os



class Linear(layers.Layer) :
    def __init__(self, units=32, input_dim=32) :
        super(Linear, self).__init__()
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(initial_value=w_init(shape=(input_dim, units), dtype=tf.float32), trainable=True)
        b_init = tf.zeros_initializer()
        self.b = tf.Variable(initial_value=b_init(shape=(units,), dtype=tf.float32), trainable=True)

    def call(self, inputs) :
        return tf.matmul(inputs, self.w) + self.b

class Linear2(layers.Layer) :
    def __init__(self, units=32, input_dim=32) :
        super(Linear2, self).__init__()
        self.w = self.add_weight(shape=(input_dim, units), initializer='random_normal', trainable=True)
        self.b = self.add_weight(shape=(units,), initializer='zeros', trainable=True)

    def call(self, inputs) :
        return tf.matmul(inputs, self.w) + self.b


class Linear3(layers.Layer) :
    def __init__(self, units=32) :
        super(Linear3, self).__init__()
        self.units = units

    def build(self, input_shape) :
        self.w = self.add_weights(shape=(input_shape[-1], self.units), initializer='random_normal', trainable=True)
        self.b = self.add_weights(shape=(self.units,), initializer='random_normal', trainable=True)

    def call(self, inputs) :
        return tf.matmul(inputs, self.w) + self.b

class ComputeSum(layers.Layer) :
    def __init__(self, input_dim) :
        super(ComputeSum, self).__init__()
        self.total = tf.Variable(initial_value=tf.zeros((input_dim,)), trainable=False)

    def call(self, inputs) :
        self.total.assign_add(tf.reduce_sum(inputs, axis=0))
        return self.total


x = tf.ones((2,2))
linear_layer = Linear2(4, 2)
y = linear_layer(x)
print(y)


x = tf.ones((2, 2))
my_sum = ComputeSum(2)
y = my_sum(x)
print(y.numpy())
y = my_sum(x)
print(y.numpy())

print('weights : ', len(my_sum.weights))
print('non-trainable weights : ', len(my_sum.non_trainable_weights))

print('trainable weights : ', my_sum.trainable_weights)

