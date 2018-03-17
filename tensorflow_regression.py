# -*- coding: utf-8 -*-
"""
Tensorflow simple regression example
Created on Sun Feb  4 16:51:08 2018

@author: Andrea Luca Lampart
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

print('Example 1: Simple multiplication node')

x = tf.constant(8)
y = tf.constant(9)
z = tf.multiply(x,y)

sess = tf.Session()

out_z = sess.run(z)

print('output: %d' % out_z)

del x,y,z,sess,out_z

print('Example 2: Linear regression model')

# Create a function with 100 points followind y= 0.2*x + 0.3 + noise
num_points = 100
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1*0.2 +0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])

# Get the first and second column vector of vectors set
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

# Create the linear regression model (A weight matrix/scalar initialized at uniform distribution)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1.0]))
y = W * x_data + b

# The loss funtion is just an L2/ Frobenius loss
loss = tf.reduce_mean(tf.square(y-y_data))

# Create a gradient descent optimizer with constant learning rate of 0.5
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

# Run session
init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)

# Train on 8 epochs
for epoch in range(100):
    #Optimize over an epoch
    session.run(train)
    # Read out graph variables
    print("Step=%d,	loss=%f,	[W=%f	b=%f]" % (epoch, session.run(loss),session.run(W),session.run(b)))
 
# Print the results
fig = plt.figure()
fig.suptitle("Regression of y = 0.2 * x + 0.3")
plot_points, = plt.plot(x_data, y_data, 'ro')
plot_line, = plt.plot(x_data, session.run(W) * x_data + session.run(b))
plt.xlabel('x')
plt.ylabel('y')
plt.legend([plot_points, plot_line], ["Dataset", "Regression"] )
plt.show()

#Close session
session.close()