import h5py
import tensorflow as tf


def data_generator(path):
    hf = h5py.File(path, 'r')
    length = hf['data'].shape[0]
    i = 0
    while i < length:
        data = hf['data'][i]
        label = hf['label'][i]
        data = tf.convert_to_tensor(data, dtype=tf.float32)
        label = tf.convert_to_tensor(label, dtype=tf.float32)
        yield data, label
        i = i + 1


def get_audio_dataset(path, batch_size, length=None):
    ds = tf.data.Dataset.from_generator(data_generator, args=[path],
                                        output_types=(tf.float32, tf.float32))
    if length is not None:
        ds = ds.shuffle(length, reshuffle_each_iteration=True).batch(batch_size)
    else:
        ds = ds.batch(batch_size)
    return ds


