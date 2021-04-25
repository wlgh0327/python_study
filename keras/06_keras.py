import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import time

inputs = keras.Input(shape=(784,), name='digits')
x1 = layers.Dense(64, activation='relu')(inputs)
x2 = layers.Dense(64, activation='relu')(x1)
outputs = layers.Dense(10, name='predictions')(x2)

model = keras.Model(inputs=inputs, outputs=outputs)

optimizer = keras.optimizers.SGD(learning_rate=1e-3)

loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)

train_acc_metric = keras.metrics.SparseCategoricalAccuracy()
val_acc_metric = keras.metrics.SparseCategoricalAccuracy()


batch_size = 64
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = np.reshape(x_train, (-1, 784))
x_test = np.reshape(x_test, (-1, 784))


x_val = x_train[-10000:]
y_val = y_train[-10000:]
x_train = x_train[:-10000]
y_train = y_train[:-10000]


train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(buffer_size=1024).batch(batch_size)

val_dataset = tf.data.Dataset.from_tensor_slices((x_val, y_val))
val_dataset = val_dataset.batch(batch_size)

epochs = 2

for epoch in range(epochs) :
    print('\nStart of epoch {}'.format(epoch))
    start_time = time.time()

    for step, (x_batch_train, y_batch_train) in enumerate(train_dataset) :
        with tf.GradientTape() as tape :

            logits = model(x_batch_train, training=True)

            loss_value = loss_fn(y_batch_train, logits)

        grads = tape.gradient(loss_value, model.trainable_weights)

        optimizer.apply_gradients(zip(grads, model.trainable_weights))

        # Update training metric
        train_acc_metric.update_state(y_batch_train, logits)

        if step % 200 == 0:
            print('Training loss (for one batch) at step {} : {:4f}'.format(step, float(loss_value)))
            print('Seen so far : {} samples'.format((step+1) * batch_size))

        train_acc = train_acc_metric.result()
        print('Training acc over epoch : {:4f}'.format(float(train_acc)))

        train_acc_metric.reset_states()

        for x_batch_val, y_batch_val in val_dataset :
            val_logits = model(x_batch_val, training=False)
            val_acc_metric.update_state(y_batch_val, val_logits)
        val_acc = val_acc_metric.result()
        val_acc_metric.reset_states()

        print('Validation acc : {:4f}'.format(float(val_acc)))
        print('Time take : {:2f}'.format(time.time() - start_time))
