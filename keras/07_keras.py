import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import os



discriminator = keras.Sequential(
        [
            keras.Input(shape=(28, 28, 1)),
            layers.Conv2D(64, (3, 3), strides=(2, 2), padding='same'),
            layers.LeakyReLU(alpha=0.2),
            layers.Conv2D(128, (3, 3), strides=(2, 2), padding='same'),
            layers.LeakyReLU(alpha=0.2),
            layers.GlobalMaxPooling2D(),
            layers.Dense(1),
            ],
        name = 'discriminator',
        )

discriminator.summary()

batch_size = 64
latent_dim = 128

generator = keras.Sequential(
        [
            keras.Input(shape=(latent_dim,)),
            layers.Dense(7*7*128),
            layers.LeakyReLU(alpha=0.2),
            layers.Reshape((7, 7, 128)),
            layers.Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same'),
            layers.LeakyReLU(alpha=0.2),
            layers.Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same'),
            layers.LeakyReLU(alpha=0.2),
            layers.Conv2D(1, (7, 7), padding='same', activation='sigmoid'),
            ],
        name = 'generator',
        )

generator.summary()


d_optimizer = keras.optimizers.Adam(learning_rate=0.0003)
g_optimizer = keras.optimizers.Adam(learning_rate=0.0004)

loss_fn = keras.losses.BinaryCrossentropy(from_logits=True)


@tf.function
def train_step(real_images) :
    random_latent_vectors = tf.random.normal(shape=(batch_size, latent_dim))

    generated_images = generator(random_latent_vectors)

    combined_images = tf.concat([generated_images, real_images], axis=0)


    labels = tf.concat([tf.ones((batch_size, 1)), tf.zeros((real_images.shape[0], 1))], axis=0)

    labels += 0.05 * tf.random.uniform(labels.shape)


    with tf.GradientTape() as tape :
        predictions = discriminator(combined_images)
        d_loss = loss_fn(labels, predictions)

    grads = tape.gradient(d_loss, discriminator.trainable_weights)
    d_optimizer.apply_gradients(zip(grads, discriminator.trainable_weights))

    random_latent_vectors = tf.random.normal(shape=(batch_size, latent_dim))
    misleading_labels = tf.zeros((batch_size, 1))

    with tf.GradientTape() as tape :
        predictions = discriminator(generator(random_latent_vectors))
        g_loss = loss_fn(misleading_labels, predictions)

    grads = tape.gradient(g_loss, generator.trainable_weights)
    g_optimizer.apply_gradients(zip(grads, generator.trainable_weights))

    return d_loss, g_loss, generated_images


(x_train, _), (x_test, _) = keras.datasets.mnist.load_data()
all_digits = np.concatenate([x_train, x_test])
all_digits = all_digits.astype('float32') / 255.0
all_digits = np.reshape(all_digits, (-1, 28, 28, 1))
dataset = tf.data.Dataset.from_tensor_slices(all_digits)
dataset = dataset.shuffle(buffer_size=1024).batch(batch_size)

epochs = 20
save_dir = './07'

if os.path.exists(save_dir) is False :
    os.makedirs(save_dir)

for epoch in range(epochs) :
    print('\nStart epoch : {}'.format(epoch))

    for step, real_images in enumerate(dataset) :
        d_loss, g_loss, generated_images = train_step(real_images)

        if step % 200 == 0 :
            print('Discriminator loss at step({}) : {:2f}'.format(step, d_loss))
            print('Adversarial loss at step({}) : {:2f}'.format(step, g_loss))

            img = tf.keras.preprocessing.image.array_to_img(generated_images[0] * 255.0, scale=False)

            img.save(os.path.join(save_dir, "generated_img_" + str(step*(epoch+1)) + ".png"))


