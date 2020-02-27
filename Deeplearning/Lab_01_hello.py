import tensorflow as tf
with tf.compat.v1.Session() as sess:

    hello = tf.constant("Hello, TensorFlow!")

    print(sess.run(hello))
