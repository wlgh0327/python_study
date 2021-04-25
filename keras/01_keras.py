import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def get_uncompiled_model() :
    inputs = keras.Input(shape=(748,), name='digits')
    x = layers.Dense(64, activation='relu', name='dense_1')(inputs)
    x = layers.Dense(64, activation='relu', name='dense_2')(x)
    outputs = layers.Dense(10, activation='softmax', name='predictions')(x)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model

def get_compiled_model() :
    model = get_uncompiled_model()
    model.compile(
            optimizer='rmsprop',
            loss='sparse_categorical_crossentropy',
            metrics=['sparse_categorical_accuracy'],
            )

    return model


def custom_mean_squared_error(y_true, y_pred) :
    return tf.math.reduce_mean(tf.square(y_true - y_pred))




if __name__ == '__main__' :

    model = get_uncompiled_model()
    model.compile(optimizer=keras.optimizers.Adam(), loss=custom_mean_squared_error)

    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    x_train = x_train.reshape(60000, 784).astype("float32") / 255
    x_test = x_test.reshape(10000, 784).astype("float32") / 255

    y_train = y_train.astype("float32")
    y_test = y_test.astype("float32")

    x_val = x_train[-10000:]
    y_val = y_train[-10000:]
    x_train = x_train[:-10000]
    y_train = y_train[:-10000]



    y_train_one_hot = tf.one_hot(y_train, depth=10)
    model.fit(x_train, y_train_one_hot, batch_size=64, epochs=1)

