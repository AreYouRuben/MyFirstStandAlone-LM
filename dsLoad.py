import tensorflow as tf
import tensorflow_datasets as tfds

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