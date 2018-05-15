title: MNIST Handwriting Detection
date: 2018-05-13
description: A fundamental exercise demonstrating machine learning from the ground up
image: /static/pictures/MNIST/head-image.png
readtime: 6 MINS
tags: [Python, Tutorial]
time: SUNDAY, MAY 13, 2018

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Data Processing Tools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

# Scikit Learn Machine Learning Tools
from sklearn.model_selection import train_test_split
from sklearn import svm

# Data Set
from mnist import MNIST
</pre>

Download the complete ipython notebook for this tutorial by clicking this [link](../static/pictures/MNIST/mnist_detection.ipynb)
