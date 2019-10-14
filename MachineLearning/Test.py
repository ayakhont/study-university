import tensorflow as tf
is_available = tf.test.is_gpu_available()
print(is_available)