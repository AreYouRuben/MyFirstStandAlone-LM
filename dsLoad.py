import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

#print(len(tf.config.list_physical_devices('GPU')))

(ds_train, ds_test), ds_info = tfds.load(
    'mnist',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(ds_info)

fig = tfds.show_examples(ds_train, ds_info)