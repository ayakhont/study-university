import tensorflow as tf

is_available = tf.test.is_gpu_available()
print(is_available)
#print(tf.config.experimental.list_physical_devices('GPU'))