#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/3/30 0030 15:20
# @Author : scw
# @File   : writenumbercompute.py
# 描述：进行手写数字的识别的实例分析
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.examples.tutorials.mnist import input_data

# 获取数据
mnist = input_data.read_data_sets("/home/zpp/download/file/MNIST_data", one_hot=True)

print('训练集信息：')
print(mnist.train.images.shape, mnist.train.labels.shape)
print('测试集信息：')
print(mnist.test.images.shape, mnist.test.labels.shape)
print('验证集信息：')
print(mnist.validation.images.shape, mnist.validation.labels.shape)

# 构建图
sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))


y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 进行训练
tf.global_variables_initializer().run()

for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	train_step.run({x: batch_xs, y_: batch_ys})

# 模型评估
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print('MNIST手写图片准确率：')
print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))







---------------------------------------------------------result-----------------------------------------------------------------------
/home/zpp/anaconda3/envs/tensorflow/bin/python /home/zpp/PycharmProjects/testformnist/writeMNIST.py
WARNING:tensorflow:From /home/zpp/PycharmProjects/testformnist/writeMNIST.py:13: read_data_sets (from tensorflow.contrib.learn.python.learn.datasets.mnist) is deprecated and will be removed in a future version.
Instructions for updating:
Please use alternatives such as official/mnist/dataset.py from tensorflow/models.
Extracting /home/zpp/download/file/MNIST_data/train-images-idx3-ubyte.gz
WARNING:tensorflow:From /home/zpp/anaconda3/envs/tensorflow/lib/python3.6/site-packages/tensorflow/contrib/learn/python/learn/datasets/mnist.py:260: maybe_download (from tensorflow.contrib.learn.python.learn.datasets.base) is deprecated and will be removed in a future version.
Instructions for updating:
Please write your own downloading logic.
WARNING:tensorflow:From /home/zpp/anaconda3/envs/tensorflow/lib/python3.6/site-packages/tensorflow/contrib/learn/python/learn/datasets/mnist.py:262: extract_images (from tensorflow.contrib.learn.python.learn.datasets.mnist) is deprecated and will be removed in a future version.
Instructions for updating:
Please use tf.data to implement this functionality.
Extracting /home/zpp/download/file/MNIST_data/train-labels-idx1-ubyte.gz
WARNING:tensorflow:From /home/zpp/anaconda3/envs/tensorflow/lib/python3.6/site-packages/tensorflow/contrib/learn/python/learn/datasets/mnist.py:267: extract_labels (from tensorflow.contrib.learn.python.learn.datasets.mnist) is deprecated and will be removed in a future version.
Instructions for updating:
Please use tf.data to implement this functionality.
WARNING:tensorflow:From /home/zpp/anaconda3/envs/tensorflow/lib/python3.6/site-packages/tensorflow/contrib/learn/python/learn/datasets/mnist.py:110: dense_to_one_hot (from tensorflow.contrib.learn.python.learn.datasets.mnist) is deprecated and will be removed in a future version.
Instructions for updating:
Please use tf.one_hot on tensors.
WARNING:tensorflow:From /home/zpp/anaconda3/envs/tensorflow/lib/python3.6/site-packages/tensorflow/contrib/learn/python/learn/datasets/base.py:252: _internal_retry.<locals>.wrap.<locals>.wrapped_fn (from tensorflow.contrib.learn.python.learn.datasets.base) is deprecated and will be removed in a future version.
Instructions for updating:
Please use urllib or similar directly.
Successfully downloaded t10k-images-idx3-ubyte.gz 1648877 bytes.
Extracting /home/zpp/download/file/MNIST_data/t10k-images-idx3-ubyte.gz
Successfully downloaded t10k-labels-idx1-ubyte.gz 4542 bytes.
Extracting /home/zpp/download/file/MNIST_data/t10k-labels-idx1-ubyte.gz
WARNING:tensorflow:From /home/zpp/anaconda3/envs/tensorflow/lib/python3.6/site-packages/tensorflow/contrib/learn/python/learn/datasets/mnist.py:290: DataSet.__init__ (from tensorflow.contrib.learn.python.learn.datasets.mnist) is deprecated and will be removed in a future version.
Instructions for updating:
Please use alternatives such as official/mnist/dataset.py from tensorflow/models.
训练集信息：
(55000, 784) (55000, 10)
测试集信息：
(10000, 784) (10000, 10)
验证集信息：
(5000, 784) (5000, 10)
MNIST手写图片准确率：
0.9198

Process finished with exit code 0
