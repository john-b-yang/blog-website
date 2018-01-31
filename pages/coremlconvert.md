title: Automated CoreML Conversion
date: 2018-01-29
description: Automating the redundancy of writing, testing, and deploying basic machine learning scripts to real world settings
image: /static/pictures/CoreMLConvert/CoreMLLogo.png
readtime: 9 MINS
time: MONDAY. JANUARY 29, 2018
tags: [ML, Python]

In recent years, the advent of machine learning has produced ripple effects felt across the software development process. Individuals and corporations have whipped up absolutely fantastic, futuristic concepts into reality with the help of machine learning tools, from [autonomous drones](https://www.nato.int/docu/review/2017/Also-in-2017/autonomous-military-drones-no-longer-science-fiction/EN/index.htm), to a [flawless Mario](https://www.youtube.com/watch?v=qv6UVOQ0F44), to the most elite [Go player](https://deepmind.com/research/alphago/) in human history!

However, while machine learning has become a familiar term, the technical strata that defines the mathematics behind it is relatively less accessible. As machine learning gains social momentum, one of the more important initiatives may become making it more comprehensible and available. Recently, Google released their [AutoML](https://cloud.google.com/automl/) product on Google Cloud Platform, allowing developers to intuitively construct and deploy their own machine learning infrastructure.

At Apple's 2017 World Wide Developer's Conference, one of many newly unveiled developer tools included [CoreML](https://developer.apple.com/videos/play/wwdc2017/703/), Apple's own integration framework allowing developers to create, train, and run customized machine learning on iOS applications. With localized ML models, apps could produce results faster, eliminating latency issues often associated with server side ML infrastructure.

However, due to this technology being relatively new, there are two inconveniences that have presented themselves: 1. There aren't that many .mlmodel files out there for use aside from some popular computer vision algorithms that can be found on Apple's [website](https://developer.apple.com/machine-learning/). 2. The documentation and code examples for CoreML conversion and potential errors is not as populated as one might hope so. With the theme of ease of use in mind, I recently pursued an initiative that I hope will make CoreML machine learning in iOS development a much easier process.

<br>
##### A Brief Primer on CoreML
Before diving into the technicalities of the application itself, I thought it'd be worthwhile to quickly explain exactly how creating a custom CoreML model works from a developer's standpoint. Keep in mind, in this article I'm discussing how to *create* a CoreML file from a Python script, not how to use one in an iOS application. Currently, Apple has a single page of official documentation [here](https://developer.apple.com/documentation/coreml/converting_trained_models_to_core_ml) that teaches you how to take ML models created with 3rd party libraries and refactor them into the ML Model format. There's a wide variety of available models, from Neural Networks to Support Vector Machines to Pipeline Models. All custom ML models must be written in Python using one of the following libraries: Scikit-learn 0.18, XGBoost 0.6, Caffe v1, Keras 1.2.2+, or LIBSVM 3.22.

Creating an MLModel file isn't all that difficult. In fact, it's a pretty redundant process. First, you'll import the corresponding libraries for the models that you're looking to convert. Then, you'll take whatever data set you're using for predictions and train the model around it. Finally, once you've trained the model, Apple's *coremltools* python [package](https://apple.github.io/coremltools/) provides a simple 'convert' function that takes in your trained Python model as a parameter and spits out an '.mlmodel' file. In code, it's as simple as running the following code. In this example, I'll be using the acclaimed Titanic data set and a Random Forest Classifier to predict which passengers survived the icy debacle (full disclosure, this model's performance is terrible and is only intended for demonstration purposes).

<pre class="inline-block prettyprint lang-py" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
# Importing Sklearn, Pandas, and Numpy Libraries
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np

# Reading Titanic Data into Pandas Dataframe
data_file = 'titanic_data.csv'
raw_data = open(data_file, 'r')
data_frame = pd.read_csv(data_file, index_col=0) # Removing index column

# Separating data into training and testing sets
y_data = data_frame[["Survived"]]
x_data = data_frame.drop(axis=1, labels=["Survived"])
X_train, X_test, Y_train, Y_test = train_test_split(x_data, y_data, train_size=split_ratio, random_state=0)

# Creating model, performing classification, and calculating performance accuracy
random_forest = RandomForestClassifier()
random_forest.fit(X_train, Y_train)
Y_prediction = random_forest.predict(Y_test)
print(classification_report(Y_test, Y_prediction))

# Converting to MLModel file
coreml_model = coremltools.converters.sklearn.convert(model, ["Pclass", "Age", "Fare"], 'survived')
coreml_model.save('TitanicSurvival.mlmodel')
</pre>

Voila! Your machine learning model is now ready to be integrated and used in your iOS application. I won't be diving too much into what that process looks like, but if your curious, Apple's official CoreML [documentation](https://developer.apple.com/documentation/coreml) gives you step by step instructions on how to get your ML model file up and running.

Before CoreML, performing machine learning on iOS went in one of two directions. You could either reimplement it entirely in Swift and Objective-C, or you could host the model for a more server side approach. Reimplementation is a tedious undertaking because of the lack of flexibility that iOS development languages have in the math and logic departments, especially when compared to a language like Python with a myriad of tailored ML and calculation libraries. A traditional server side approach allows for more flexibility in your model, but it comes at a tradeoff. Latency and reliability. will perpetually be an issue. In addition, maintaining a server could be an expensive and unscalable solution that becomes a greater headache as an app gains users (which should be a good thing)!

CoreML represents the best of both worlds. As a localized file that sits within your app, it eliminates the latency and scalability qualms of server side solutions, allowing you to front load any ML work onto your users' devices as opposed to your own. In addition, the ability to convert models preserves the flexibility that comes with Python written code. In addition, an MLModel is optimized for fast performance by the iOS architecture itself. Hopefully, I've convinced you somewhat of how much of a game changer CoreML is.

<br>
##### Automating CoreML's solution
Highlighting the redundancy behind custom scripts for generating CoreML files

<br>
##### Designing a Flexible Script for ML Testing
Discuss what goes in, how it's processed, and what comes out

<br>
##### Decorations: An Accessible Platform
Flask + HTML/CSS!

<br>
##### What's Next?
Design + What More Flexibility Looks Like / Demands
