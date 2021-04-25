import numpy as np
import os
import tensorflow as tf
from tensorflow import keras

def get_model() :
    inputs = keras.Input(shape=(32,))
    outputs = keras.layers.Dense(1)(inputs)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def test1() :
    model = get_model()

    test_input = np.random.random((128, 32))
    test_target = np.random.random((128, 1))
    model.fit(test_input, test_target)


    if not os.path.exists('./model') :
        os.makedirs('./model')

    model.save('./model/my_model')

    reconstructed_model = keras.models.load_model('./model/my_model')




    np.testing.assert_allclose(
            model.predict(test_input), reconstructed_model.predict(test_input)
            )


    reconstructed_model.fit(test_input, test_target)


class CustomModel(keras.Model) :
    def __init__(self, hidden_units) :
        super(CustomModel, self).__init__()
        self.dense_layers = [keras.layers.Dense(u) for u in hidden_units]

    def call(self, inputs) :
        x = inputs
        for layer in self.dense_layers :
            x = layer(x)
        return x

if __name__ == '__main__' :
    #test1()
    print('============')
    #model = CustomModel([16, 16, 10])
    model = CustomModel([16, 16, 100])
    input_arr = tf.random.uniform((1, 5))
    outputs = model(input_arr)

    if not os.path.exists('./model') :
        os.makedirs('./model')

    #model.save('./model/my_model2')

    keras.utils.plot_model(model, 'test2.png', show_shapes=True)

    del CustomModel

    loaded = keras.models.load_model('./model/my_model2')
    #np.testing.assert_allclose(loaded(input_arr), outputs)

    print('Original model : ', model)
    print('Loaded model : ', loaded)

    keras.utils.plot_model(loaded, 'test22.png', show_shapes=True)

    print(model.summary())
    print(loaded.summary())

    print(model.get_config())

    print(loaded.get_config())
