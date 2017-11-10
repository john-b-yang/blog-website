title: Twitter Bot!
date: 2017-11-08
tags: [Python, Tutorial]
description: Markov Chains meet Flask meet Twitter API for a simple, mathematical web program

#### Links
- [Twitter Bot](https://twitter.com/vernesnautilus)
- [Github Repository](https://github.com/MakeSchool-17/twitter-bot-python-john-b-yang)
- [Tweet Generator](https://fast-headland-20951.herokuapp.com)

<br>
#### Step 1: Selecting + Cleaning a Corpus
The initial step to creating a successful Twitter Bot depends on finding a repository of words that your bot can emulate. The primary features of this text emphasize consistency and word count. A large amount of text increases the grammatical and contextual patterns that the bot can identify and emulate. To put it simply, the lengthier the book, the richer the sentences. From experimenting with different texts, I'd recommend at least a document of at least ten thousands words.

For a basic bot, any lengthy novel should suffice. A good place to start would be classical literature. These texts satisfy that 10000 word threshold, but are not so long that text processing takes an inordinate amount of time. In addition, these books are consistently rich in style, so the sentences your chatbot generates will have its own unique and quirky dialect. Usually, you can find online copies of these books in the form of web pages and PDFs. For our purposes, it's better if you find a web page, as it makes the process of reading and parsing the text relatively easier compared to a PDF source. [Project Gutenberg](http://www.gutenberg.org) and many universities' online libraries are excellent places to look.

When you've found a book you like, look into the [Diffbot API](https://www.diffbot.com/products/) for parsing and cleaning up the text. It's a fantastic web crawling API that allows you to download and filter a website's source code. The [generate_corpus.py](http://bit.ly/2zvTTNw) file in my Github repository details how I performed text extraction and clean up. Make sure to remove superfluous HTML tags and unknown characters. It's also important to take into account the context of your text. Ask yourself whether certain characters should actually be removed. For example, while it's reasonable to eliminate "<" or ">" characters if they are part of html tags, given a different context such as a math textbook, the two could be serving as comparison operators. After cleaning the text, store the resulting body inside a text file.

*Files*: book_sample.txt, generate_corpus.py

<br>
#### Step 2: Corpus Parsing and Tokenization
After Step 1, you've successfully read the source code of the website containing your desired text, cleaned your text of superfluous HTML text and unknown characters, and stored the output into a text file. Now, the next task involves converting this book into a navigable, random, and representative data structure that can be used to generate grammatically sound sentences that emulate our text. Introducing, [Markov Chains](https://en.wikipedia.org/wiki/Markov_chain).

The Markov Chain is a structure that falls under the domain of discrete math and probability. There is a plethora of mathematics and applications that I highly recommend diving into (Google's PageRank algorithm, the backbone of Search, is a Markov Process!). However, for the sake of this tutorial, we'll use Markov Chains primarily for how it can make future predictions of a state based on its present state. To illustrate this concept, let's say we're given a sentence "I eat fast, you eat slow, I eat fast, I eat slow". A Markov Chain can be thought of as a graph-like snapshot of the structure of this sentence, where each node is a word and each edge is a probability reflecting the likelihood of one word coming after another one.

<br>
![](/static/pictures/MarkovChain.png)

<br>
In the original sentence, the word 'I' appears three times, and it is followed by the word 'eat' all three times. Therefore, there is a probability of 3/3 or 1 that any random traversal of the map involving 'I' will be followed by 'eat'. On the other hand, 'fast' appears two times, followed by 'you' and 'I' respectively. Therefore, there is a 1/2 probability that a random traversal from 'fast' results in 'I', and a 1/2 probability it results in 'you'. In this step of the program, we will be applying the same logic from above to an entire book. In Step 3, we will generate a random sentence by performing a traversal on the resulting Markov Chain representation of the book.



*Files*: tokenize.py, make_sentence.py

<br>
#### Step 3: Generate a Sentence

We would be doing the same operation, but instead on the entire book. As you can imagine, the Markov Chain would be quite large. When creating the Markov Chain, it's important to think about what data structures you might use to store it. Personally, I used a dictionary where each key was a word, and the value was a sub-dictionary. The sub dictionary has a word as a key and the number of appearances as its value.

When it comes to randomly generating a sentence, it's important to identify two kinds of words. The first is "start points" aka words that only have outward pointing arrows. We use these words as the beginnings to our sentence. Subsequently, we also have "end points", words with only inward pointing arrows. These words terminate the sentence, as there are no words that could follow. Having these two points is important for maintaining grammatical consistency in our sentences.

*Files*: make_sentence.py

#### Step 4: Twitter API

Twitter has excellent documentation on how to use their API, and by exploring it more in depth, you can probably come up with much more impressive use cases. However, for this particular project, I focused on posting a simple tweet using a python module. There are four different kinds of keys required to establish a session with your linked twitter account. With the right url, a simple "post" method call is all that's needed to pass in a sentence to be placed on the account. Note that the 140 character limit is in effect, so posts that exceed the limit may incur an error code during the requests call.

Quick Note, I do recommend storing the keys within a hidden file as opposed to copy and pasting them directly into your code, especially if you plan on open sourcing the code in the future. To protect your private account keys, store the in a hidden file, then set them as environment variables within your virtualenv. That allows you to reference the key values as environment variables in your code, so while you maintain access, other people will not be able to appropriate your keys if you happen to put the code on Github. Make sure to list hidden files in your gitignore.

*Files*: twitter.py

<br>
#### Step 5: Flask Development

The point of adding a Flask app to this project is to give other people the capability to generate and tweet sentences for your bot. I used the barebone functionality of a Flask server paired with an index.html template to simply display the randomly generated sentence along with a "tweet this" button. If you're like me and not very well versed in web development, i'd definitely recommend Flask for its simplicity and straightforward customizability. It's up to you how you'd like to host your code. I went with Heroku, as they have a good amount of documentation to walk you through deploying Flask driven development.

*Files*: Procfile, requirements.txt, runtime.txt, server.py, app.py

<br>
#### Step 6: Scripting

At this, your bot is decked out. Let's just say, a month later, you want to show it off to a couple friends. Unfortunately, no one has visited your website, and you haven't bothered tweeting in a while. This is where scripting comes in. I wrote a simple shell script that runs a python script which sends a tweet. By scheduling that shell script in your cronjob directory, you'll have a bot that tweets consistently, and your project will update itself, hands free!

*Files*: tweetjob.py, tweetscript.sh, output.txt
