import tensorflow as tf
with tf.compat.v1.Session() as sess:
    # x_train = [1,2,3]
    # y_train = [1,2,3]

    X = tf.compat.v1.placeholder(tf.float32, shape=[None]) # , shape=[None]은 갯수 제한 없다는 뜻
    Y = tf.compat.v1.placeholder(tf.float32, shape=[None])


    # .Variable은 TensorFlow가 스스로 변경하며 사용하는 변수
    W = tf.Variable(tf.compat.v1.random_normal([1]), name='weight')
    b = tf.Variable(tf.compat.v1.random_normal([1]), name='bias')

    hypothesis = X * W + b

    # .reducemean은 평균 내주는 것
    cost = tf.reduce_mean(tf.square(hypothesis - Y))

    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.01)
    train = optimizer.minimize(cost)

    sess.run(tf.compat.v1.global_variables_initializer())

    for step in range(2001):
        cost_val, W_val, b_val, _ = sess.run([cost, W, b, train], feed_dict={X:[1,2,3,4,5], Y:[2.1,3.1,4.1,5.1,6.1]})
        # sess.run(train)
        if step % 20 == 0:
            # print(step, sess.run(cost), sess.run(W), sess.run(b))
            print(step, cost_val, W_val, b_val)

    
    # 결과값 체크
    print(sess.run(hypothesis, feed_dict={X:[5]}))
