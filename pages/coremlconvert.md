title: Automated CoreML Conversion
date: 2018-01-29
description: Automating the redundancy of writing, testing, and deploying basic machine learning scripts to real world settings
image: /static/pictures/CoreMLConvert/CoreMLLogo.png
readtime: 5 MINS
time: MONDAY. JANUARY 29, 2018
tags: [ML, Python]

In recent years, the advent of machine learning has produced ripple effects felt across the software development process. Individuals and corporations have whipped up absolutely fantastic, futuristic concepts into reality with the help of machine learning tools, from [autonomous drones](https://www.nato.int/docu/review/2017/Also-in-2017/autonomous-military-drones-no-longer-science-fiction/EN/index.htm), to a [flawless Mario](https://www.youtube.com/watch?v=qv6UVOQ0F44), to the most elite [Go player](https://deepmind.com/research/alphago/) in human history!

However, while machine learning has become a familiar term, the technical strata that defines the mathematics behind it is relatively less accessible. As machine learning gains social momentum, one of the more important initiatives may become making it more comprehensible and available. Recently, Google released their [AutoML](https://cloud.google.com/automl/) product on Google Cloud Platform, allowing developers to intuitively construct and deploy their own machine learning infrastructure.

At Apple's 2017 World Wide Developer's Conference, one of many newly unveiled developer tools included [CoreML](https://developer.apple.com/videos/play/wwdc2017/703/), Apple's own integration framework allowing developers to create, train, and run customized machine learning on iOS applications. With localized ML models, apps could produce results faster, eliminating latency issues often associated with server side ML infrastructure.

However, due to this technology being relatively new, there are two inconveniences that have presented themselves: 1. There aren't that many .mlmodel files out there for use aside from some popular computer vision algorithms that can be found on Apple's [website](https://developer.apple.com/machine-learning/). 2. The documentation and code examples for CoreML conversion and potential errors is not as populated as one might hope so. With the theme of accessibility in mind, I recently pursued an initiative that I hope will make CoreML machine learning in iOS development a much easier process.

<br>
##### A Brief Primer on CoreML
Discussing what CoreML is and localized iOS dev vs. remote servers

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
