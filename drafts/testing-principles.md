title: Principles of Testing | Unit Tests
date: 2018-06-04
description: A unit test a day keeps the null pointer exceptions away.
image: /static/pictures/UnitTests/UnitTestLogo.jpeg
readtime: 6 MINS
tags: [Testing]
time: WEDNESDAY, JUNE 20, 2018

This past semester as a student at UC Berkeley, I took a computer science course titled "CS61C: Great Ideas in Computer Architecture". This course servers as a primer for the C programming language. It dives into the so called "low level" machine structures that hosts the nitty gritty details of "what" and "how" a computer works. CS61C is known for having a handful of long projects. In my opinion, the challenge for doing well was two fold. First, the implementation for these solutions were very lengthy. Second, due to the lack of scaffolding, it became common for work in progress to start veering in the wrong direction.

To be honest, I felt pretty overwhelmed when faced with a task that is characterized by dangerous degrees of freedom. Too many times, I found myself spending hours writing an implementation from scratch to completion, only to find out that it was the incorrect approach.

At Google, there's a company-wide emphasis on writing robust, comprehensive tests. Most code waiting to be checked in is complemented by a suite of tests.

In this article, I hope my experience portrays testing as an intuitive, logical art form. Testing is, and should be a lot easier than a university Operating Systems or Machine Learning class. This article's true purpose is to introduce mainstream industry concepts, structures, and conventions that helped shape my raw, initial instincts towards the art of software testing.

##### Basic Terminology

Wikipedia provides a pretty well rounded definition of unit testing: "In computer programming unit testing is a software testing method by which individual units of source code, sets of one or more computer program modules...are tested to determine whether they are fit for use."

Michael Feathers, author of "Working Effectively with Legacy Code", describes good unit tests as: "they run fast, they help us localize problems". In other words, unit tests are meant to be lightweight and specific with surgical precision. If an effective unit test fails, it directly points out the code responsible for the failure. No extra debugging should be required to diagnose the cause of a unit test failure.

So what does "lightweight" exactly mean? A general rule of thumb is that unit tests should not be overly reliant on external dependencies or frameworks that are outside the realm of the class being tested. Practically speaking, unit tests don't require communicating on a network or switching between processes (see [integration testing](https://en.wikipedia.org/wiki/Integration_testing)). When we discuss testing on this level, we're intentionally limiting our scope to just the class itself. Respecting this contextualization is what makes unit tests bit-sized simple and yet absolute in its pass/fail results.

##### Goals of a Unit Test



##### Anatomy of a Unit Test

TODO(john-b-yang) Include basic example here

##### Name Unit Tests Intuitively

For any class, it's never a bad idea to write a corresponding set of test methods. Each method's name conveys a responsibility of the object, as opposed to the class's methods or inputs/outputs themselves. Keep in mind that the point of unit tests are to serve as small, testable modules that can be run independently from one another. Unit tests are there to ensure that code meets design and behavior guidelines, *not* the durability of one particular function. Great unit tests are straightforward enough that someone else reading your code can understand its purpose without needing to dive into the implementation itself.

Here's an example of a Java class testing different aspects of a time format conversion class.

<pre class="prettyprint lang-java background">
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

In Dr. Robert Cecil Martin's book, [Clean Code](https://www.investigatii.md/uploads/resurse/Clean_Code.pdf), Dr. Martin discusses an idea called the "Single Responsibility Principle". This principle encourages readable, simple code by enforcing a standard which states that every module has responsibility over one and only one part of the software's functionality. I thought about it this way: Imagine you're a watchmaker designing the mechanism for turning the hour and minute hands. By Dr. Martin's principle, it's better to have multiple small cogs rather than one large cog powering each tick (It's not a very realistic analogy, but hopefully it illustrates his point more vividly).

The Single Responsibility Principle has merit across the software development board. When it comes to maintenance, bit-sized modules of code makes it easier to identify points of failure. Microservices' emphasis on designing software as individual, isolated services with singular purposes is what makes this architecture so favorable for deploying and maintaining production code. In his article "Understanding Microservices", Michael Douglass makes a fantastic point on how "Complexity [in monolithic codebases] comes from low cohesion and high coupling". Tying things back to this article, unit tests are perfectly in line with this ideology.

However, the more modularized code is, the more inevitable inter-class dependencies become. In the context of unit testing, the parameters and libraries that modules are reliant on become obstacles to the incubated nature of unit tests. But not to worry, the solution is entertainingly simple: Fake it till you make it!

Instead of having to deal with time consuming dependencies, you can substitute in custom objects to help thoroughly test your code, increase coverage, and execute tests at superior speeds. Creating custom objects frees you from expectations and limitations that might be projected by dependencies. For example, creating a custom object can allow you to simulate rare edge case dependency failures that otherwise could not be offered by a service that has to be up and running.

There's an excerpt of Gerard Meszaros that I thought provided a great, pithy explanation behind the problem and solution to module dependencies:

"Sometimes it is just plain hard to test the system under test (SUT) because it depends on other components that cannot be used in the test environment. This could be because they aren’t available, they will not return the results needed for the test or because executing them would have undesirable side effects. In other cases, our test strategy requires us to have more control or visibility of the internal behavior of the SUT.  When we are writing a test in which we cannot (or chose not to) use a real depended-on component (DOC), we can replace it with a Test Double. The Test Double doesn’t have to behave exactly like the real DOC; it merely has to provide the same API as the real one so that the SUT thinks it is the real one!"

"Custom Objects" is a broad term that encompasses a variety of mock testing components. In his book [xUnit Test Patterns](https://martinfowler.com/books/meszaros.html), author Gerard Meszaros identifies a couple categories and definitions for different custom objects.
- Test Double: Test object that replaces a production object
- Dummy: Objects that are passed around by not actually used. The best example is as fillers for parameter lists.
- Fakes: Components with semi-working implementations. They work well enough to run a test, but take shortcuts to cut out irrelevant functionalities.
- Stubs: Canned answers to calls made during a test. For instance, an artificial server with the same response to a post request.
- Mocks: Expectations which form a specification of the calls they do and do not receive.
