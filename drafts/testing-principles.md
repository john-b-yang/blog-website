title: Principles of Testing (Pt. 1 - Unit Tests)
date: 2018-06-04
description: A unit test a day keeps the exceptions away.
image: /static/pictures/MNIST/head-image.png
readtime: 6 MINS
tags: []
time: WEDNESDAY, JUNE 20, 2018

This past semester as a student at UC Berkeley, I took a computer science course titled "CS61C: Great Ideas in Computer Architecture". This course servers as a primer for the C programming language. It dives into the so called "low level" machine structures that hosts the nitty gritty details of "what" and "how" a computer works. CS61C is known for having a handful of long projects. In my opinion, the challenge for doing well was two fold. First, the implementation for these solutions were very lengthy. Second, due to the lack of scaffolding, it became common for work in progress to start veering in the wrong direction.

To be honest, I felt pretty overwhelmed when faced with a task that is characterized by dangerous degrees of freedom. Too many times, I found myself spending hours writing an implementation from scratch to completion, only to find out that it was the incorrect approach.

At Google, there's a company-wide emphasis on writing robust, comprehensive tests. Most code waiting to be checked in is complemented by a suite of tests.

##### Basic Terminology

Wikipedia provides a pretty well rounded definition of unit testing: "In computer programming unit testing is a software testing method by which individual units of source code, sets of one or more computer program modules...are tested to determine whether they are fit for use."

Michael Feathers, author of "Working Effectively with Legacy Code", describes good unit tests as: "they run fast, they help us localize problems". In other words, unit tests are meant to be lightweight and specific with surgical precision. If an effective unit test fails, it directly points out the code responsible for the failure. No extra debugging should be required to diagnose the cause of a unit test failure.

So what does "lightweight" exactly mean? A general rule of thumb is that unit tests should not be overly reliant on external dependencies or frameworks that are outside the realm of the class being tested. Practically speaking, unit tests don't require communicating on a network or switching between processes (see [integration testing](https://en.wikipedia.org/wiki/Integration_testing)). When we discuss testing on this level, we're intentionally limiting our scope to just the class itself. Respecting this contextualization is what makes unit tests bit-sized simple and yet absolute in its pass/fail results.

##### Anatomy of a Unit Test

TODO(john-b-yang) Include basic example here

##### Name Unit Tests Intuitively

For any class, it's never a bad idea to write a corresponding set of test methods. Each method's name conveys a responsibility of the object, as opposed to the class's methods or inputs/outputs themselves. Keep in mind that the point of unit tests are to serve as small, testable modules that can be run independently from one another. Unit tests are there to ensure that code meets design and behavior guidelines, *not* the durability of one particular function. Great unit tests are straightforward enough that someone else reading your code can understand its purpose without needing to dive into the implementation itself.

Here's an example of a Java class testing different aspects of a time format conversion class.

<pre class="inline-block prettyprint lang-java" style="background-color: rgb(236, 243, 249);border: none;border-radius: 10px;padding: 15px;">
class DateTimeConverterTest {
    void testConvertsUTCToPST () {...}
    void testThrowsExceptionIfIncorrectFormat () {...}
    void testDoesNotModifyTimeParameter () {...}
}
</pre>

In this format, testing code is much more readable. When someone else reviews your test code, it almost feels like they're reading a README description of the behavioral expectations of the code. For instance, given the above structure,
- Date Time Converter converts UTC to PST.
- Date Time Converter throws exception if incorrect format.
- Date Time Converter does not modify time parameter.

##### Overcoming Module Dependencies

TODO(john-b-yang) Discuss the inevitability of how classes are interdependent. Introduce and create examples for terms: test double, dummy, fakes, stubs, mocks.
