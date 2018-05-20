title: MNIST Handwriting Detection
date: 2018-05-13
description: Exploring different machine learning models through the "Hello World" of data sets
image: /static/pictures/MNIST/head-image.png
readtime: 6 MINS
tags: [Python, Tutorial]
time: SUNDAY, MAY 13, 2018

In this article, my goal is to use the MNIST Classification problem as a conduit for building practical analogies that illustrate how different machine learning models perform. By using one of the most rudimentary, introductory data set out there, I hope to highlight some of the tradeoffs that come with different approaches to a very traditional classification problem.

##### Part 1: Data Processing Tools

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Data Processing Tools
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import Counter

# Scikit Learn Machine Learning Tools
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import svm

# Data Set
from mnist import MNIST

%matplotlib inline

# Suppress Warnings
import warnings
warnings.filterwarnings('ignore')
</pre>

##### Part 2: MNIST Data Organization

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
mndata = MNIST('/Users/johnyang/Desktop/')
mnist_images, mnist_labels = mndata.load_testing()

# Create DataFrame with 784 (28x28 Image) columns and 10000 rows
# Column = feature / color of pixel at specific index
# Row = One instance of data
mnist_df = pd.DataFrame(mnist_images)

# Add labels corresponding to images as last column in table
mnist_df.insert(loc=0, column='label', value=mnist_labels)

# Separate image pixel values and labels
# Take first 5000 images b/c ain't nobody got time for 10000 images
images = mnist_df.iloc[0:5000, 1:]
labels = mnist_df.iloc[0:5000, :1]

# Randomly separate data into testing and training batches
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, train_size=0.5, random_state=0)

# Cast pandas array types into numpy arrays to make it easier to run computations
train_images_array = train_images.as_matrix()
test_images_array = test_images.as_matrix()
train_labels_array = train_labels.as_matrix()
</pre>

##### Part 3: Data Visualization

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Select first image from training set
image = train_images.iloc[0].as_matrix()

# Reshape 784x1 row into 28x28 matrix / image
image = image.reshape((28, 28))

# Visual Representation of one instance of the data
plt.imshow(image, cmap='gray')
plt.title(train_labels.iloc[0, 0])

# Histogram Plot representing Distribution of Data
plt.hist(train_images.iloc[0])
</pre>

##### Part 4: K Nearest Neighbors

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
test_images_len = test_images.shape[0]
predictions = []

batch_size = 250
batches = int(test_images_len/batch_size)

print("Number of batches: " + str(batches))
for i in range(int(batches)):
    # Time of batch processing speed
    tick = time.time()

    # Euclidean Distance Calculation
    test_prediction = test_images_array[(i * batch_size):((i+1) * batch_size)]
    dot_product = np.dot(test_prediction, train_images_array.T)
    sum_square_test = np.square(test_prediction).sum(axis=1)
    sum_square_train = np.square(train_images_array).sum(axis=1)
    distances = np.sqrt(-2 * dot_product + sum_square_train + np.matrix(sum_square_test).T)

    num_distances = distances.shape[0]

    # Batch Predictions
    label_predictions = np.zeros(num_distances)
    for j in range(num_distances):
        k_closest_y = []
        # Labels from points with distance calculated
        calculated_labels = train_labels_array[np.argsort(distances[j,:])].flatten()
        # 3 Closest Neighbors
        k_closest_y = calculated_labels[:3]
        # Count Unique Neighbors
        counted = Counter(k_closest_y)
        label_predictions[j] = counted.most_common(1)[0][0]
    predictions = predictions + list(label_predictions)
    tock = time.time()
    print("Completed batch " + str(i + 1) + "/" + str(batches) + " in " + str(tock - tick) + " Seconds.")
</pre>

##### Part 5: Support Vector Machine

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Trial 1: Apply SVM to raw data set
svm_classifier = svm.SVC()
svm_classifier.fit(train_images, train_labels.values.ravel())
accuracy = svm_classifier.score(test_images, test_labels)
print(str(round(accuracy, 4)))
</pre>

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Denoising number boundaries to be more clear
test_images[test_images > 0] = 1
train_images[train_images > 0] = 1
</pre>

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Trial 2: Apply SVM to binary data set
svm_classifier = svm.SVC()
svm_classifier.fit(train_images, train_labels.values.ravel())
accuracy = svm_classifier.score(test_images, test_labels)
print("Accuracy: " + str(round(accuracy, 4)))
print(classification_report(train_labels, predictions))
</pre>

##### Part 6: Logistic Regression

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
</pre>

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Placeholder: Value to be input when asking TensorFlow to run computation
x = tf.placeholder(tf.float32, [None, 784])

# Variable: Modifiable tensor living in the TensorFlow graph
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Softmax Regression!
y = tf.nn.softmax(tf.matmul(x, W) + b)
</pre>

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Cost / Loss Function: How far off our model is from desired outcome

# Cross-entropy: Measures how inefficient predictions are for describing the truth
# Function = - summation (y' * log(y))
y_prime = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_prime * tf.log(y), reduction_indices=[1]))

# Minimize cross_entropy function with gradient descent + 0.5 Learning Rate
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
</pre>

View the complete ipython notebook for this tutorial by following this [link](https://github.com/john-b-yang/blog-website/blob/master/static/misc/mnist-detection.ipynb)!
