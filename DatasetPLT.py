from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import random

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

image = X_train[random.randint(1,100)]


plt.imshow(image, cmap='gray')
plt.show()