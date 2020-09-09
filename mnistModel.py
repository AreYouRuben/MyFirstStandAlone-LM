import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import random
import argparse
import pickle

#Code based on the following links:
#https://www.tensorflow.org/api_docs/python/tf/keras
#https://www.udemy.com/course/deep-learning-tensorflow-2/

ap = argparse.ArgumentParser()
ap.add_argument("--mode",help="train/display")
mode = ap.parse_args().mode

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print("x_train.shape:", x_train.shape)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

if mode == "train":
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    r = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10)
    model.save('saved_model\my_model')
    
    np.save('ModelHistory\history_sim#', r.history)

    plt.plot(r.history['loss'], label='loss')
    plt.plot(r.history['val_loss'], label='val_loss')
    plt.legend()
    plt.show()

elif mode == "display":
    new_model = tf.keras.models.load_model('saved_model\my_model')
    new_model.summary()
    loss, acc = new_model.evaluate(x_test, y_test, verbose=2)
    print('Restored model, accuracy: {:5.2f}%'.format(100*acc))

    r = np.load('ModelHistory\history_sim#.npy',allow_pickle=True).item()

    plt.plot(r['loss'], label='loss')
    plt.plot(r['val_loss'], label='val_loss')
    plt.legend()
    plt.show()
