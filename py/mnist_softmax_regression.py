# 导入TensorFlow
import tensorflow as tf
# 读取数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# x是占位符
x = tf.placeholder("float", [None, 784])

# W b是变量，代表可修改的张量，可以用于计算输入值，也可以在计算中被修改。
# 用全为零的张量来初始化W和b。因为我们要学习W和b的值，它们的初值可以随意设置。
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 用tf.matmul(​​X，W)表示x乘以W
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 标签
y_ = tf.placeholder("float", [None, 10])

# 首先，用 tf.log(y)计算y中每个元素的对数。
# 接下来，我们把y_的每一个元素和tf.log(y)的对应元素相乘。最后，用tf.reduce_sum计算张量的所有元素的总和。
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

# 用梯度下降算法（GD）以0.01的学习速率最小化交叉熵。
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 添加一个操作来初始化我们创建的变量
init = tf.initialize_all_variables()

# 在一个Session里面启动我们的模型，并且初始化变量：
sess = tf.Session()
sess.run(init)

# 开始训练模型，这里我们让模型循环训练1000次
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

'''
tf.argmax给出某个tensor对象在某一维上的其数据 最大值 所在的索引值。
比如tf.argmax(y,1)返回的是模型对于任一输入x预测到的标签值，而 tf.argmax(y_,1) 代表正确的标签，
我们可以用 tf.equal 来检测我们的预测是否真实标签匹配(索引位置一样表示匹配)。
'''
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

# 把布尔值转换成浮点数，然后取平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# 计算所学习到的模型在测试数据集上面的正确率
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
