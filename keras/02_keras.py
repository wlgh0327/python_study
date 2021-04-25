import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import os

checkpoint_dir = './ckpt'
logdir = './logs'
if not os.path.exists(checkpoint_dir) :
    os.makedirs(checkpoint_dir)

def get_uncompiled_model() :
    image_input = keras.Input(shape=(32, 32, 3), name='img_input')
    timeseries_input = keras.Input(shape=(None, 10), name='ts_input')

    x1 = layers.Conv2D(filters=16, kernel_size=(3,1), padding='same')(image_input)
    x1 = layers.Conv2D(filters=16, kernel_size=(1,3), padding='same')(x1)
    x1 = layers.Conv2D(filters=3, kernel_size=3)(x1)
    x1 = layers.GlobalMaxPooling2D()(x1)

    x2 = layers.Conv1D(3, 3, padding='same')(timeseries_input)
    x2 = layers.GlobalMaxPooling1D()(x2)

    x = layers.concatenate([x1, x2])

    score_output = layers.Dense(1, name='score_output')(x)
    class_output = layers.Dense(5, name='class_output')(x)

    model = keras.Model(inputs=[image_input, timeseries_input], outputs=[score_output, class_output])

    return model

def get_compiled_model() :
    model = get_uncompiled_model()

    model.compile(optimizer=keras.optimizers.RMSprop(1e-3),
            loss = {
                'score_output' : keras.losses.MeanSquaredError(),
                'class_output' : keras.losses.CategoricalCrossentropy(),
                },
            metrics = {
                'score_output' : [
                    keras.metrics.MeanAbsolutePercentageError(),
                    keras.metrics.MeanAbsoluteError(),
                    ],
                'class_output' : [keras.metrics.CategoricalAccuracy()],
                },
            loss_weights = {'score_output' : 1.0, 'class_output' : 1.0},
            )

    return model


def make_or_restore_model() :
    checkpoints = [checkpoint_dir + '/' + name for name in os.listdir(checkpoint_dir)]
    if checkpoints :
        latest_checkpoint = max(checkpoints, key=os.path.getctime)
        print('Restoring from', latest_checkpoint)
        return keras.models.load_model(latest_checkpoint)
    print('creating a new_model')
    return get_compiled_model()


model = make_or_restore_model()
callbacks = [
        keras.callbacks.ModelCheckpoint(filepath=checkpoint_dir + '/{epoch}_ckpt-loss={loss:2f}', save_freq=100),
        keras.callbacks.TensorBoard(log_dir=logdir, histogram_freq=0, embeddings_freq=0, update_freq='epoch',),
        ]
keras.utils.plot_model(model, "multi_input_and_output_model.png", show_shapes=True)


#model.compile(optimizer=keras.optimizers.RMSprop(1e-3),
        #loss=[keras.losses.MeanSquaredError(), keras.losses.CategoricalCrossentropy()],)
#



img_data = np.random.random_sample(size=(10000, 32, 32, 3))
ts_data = np.random.random_sample(size=(10000, 20, 10))
score_targets = np.random.random_sample(size=(10000, 1))
class_targets = np.random.random_sample(size=(10000, 5))

model.fit(
        {'img_input' : img_data, 'ts_input' : ts_data},
        {'score_output' : score_targets, 'class_output' : class_targets},
        batch_size=32,
        epochs=10,
        callbacks=callbacks,
        )
