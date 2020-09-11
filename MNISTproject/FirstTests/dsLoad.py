import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import numpy as np
#Put on VSC terminal to activate virtualenv after
#   Set-ExecutionPolicy Unrestricted -Scope Process

#print(len(tf.config.list_physical_devices('GPU')))

###### Shows a grid with different examples
# (ds_train, ds_test), ds_info = tfds.load(
#     'mnist',
#     split=['train', 'test'],
#     shuffle_files=True,
#     as_supervised=True,
#     with_info=True,
# )
#print(ds_info)
#fig = tfds.show_examples(ds_train, ds_info)

###### This does the same as DatasetPLT.py with more code
dataset = tfds.load('mnist')
train, test = dataset['train'], dataset['test']
dsnp = np.vstack(tfds.as_numpy(test))

X_test = np.array(tuple(map(lambda x: x[0]['image'], dsnp)))
y_test = np.array(tuple(map(lambda x: x[0]['label'], dsnp)))
plt.imshow(X_test[1], cmap='gray')
plt.show()