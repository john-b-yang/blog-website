title: Twitter Bot
date: 2017-11-08
tags: [python, machine learning]

[Twitter Bot Link](https://twitter.com/vernesnautilus)

#### Step 1: Selecting a Corpus
The whole foundation of the twitter bot depends on finding a repository of words that a bot could emulate. The corpus must exhibit a certain degree of consistency while containing enough words that a pattern can be imitated. The size of the corpus should be more than 10000 words for our bot to record patterns during sentence generation.

Files: book_sample.txt, generate_corpus.py

#### Step 2: Corpus Parsing and Tokenization
Before tokenizing and mapping the text, it's important to clean up the text first. Especially if the text is retrieved from a website, make sure to remove superfluous HTML tags and unknown characters. Given the body of work for your corpus, it's also important to take into account the context of the text, and ask whether certain characters should actually be removed. For example, while it's reasonable to eliminate "<" or ">" characters if they are part of html tags, given a different context such as a math textbook, the two could be serving as greater than, less than signs.

Files: book_sample.txt, tokenize.py

#### Step 3: Generate a Sentence

Now, after successfully reducing the original corpus to its core segments, we need a way to traverse through words in a grammatical fashion that emulates the speaker. To do this, we can use a construct called Markov Chains. A simple understanding of a Markov Chain in this context would be creating a map of a word. For example, given a sentence "I eat fast, you eat slow, I eat fast, I eat slow", the resulting Markov Chain would look like such:

![](/static/pictures/MarkovChain.png)

We would be doing the same operation, but instead on the entire book. As you can imagine, the Markov Chain would be quite large. When creating the Markov Chain, it's important to think about what data structures you might use to store it. Personally, I used a dictionary where each key was a word, and the value was a sub-dictionary. The sub dictionary has a word as a key and the number of appearances as its value.

When it comes to randomly generating a sentence, it's important to identify two kinds of words. The first is "start points" aka words that only have outward pointing arrows. We use these words as the beginnings to our sentence. Subsequently, we also have "end points", words with only inward pointing arrows. These words terminate the sentence, as there are no words that could follow. Having these two points is important for maintaining grammatical consistency in our sentences.

Files: make_sentence.py

#### Step 4: Twitter API

Twitter has excellent documentation on how to use their API, and by exploring it more in depth, you can probably come up with much more impressive use cases. However, for this particular project, I focused on posting a simple tweet using a python module. There are four different kinds of keys required to establish a session with your linked twitter account. With the right url, a simple "post" method call is all that's needed to pass in a sentence to be placed on the account. Note that the 140 character limit is in effect, so posts that exceed the limit may incur an error code during the requests call.

Quick Note, I do recommend storing the keys within a hidden file as opposed to copy and pasting them directly into your code, especially if you plan on open sourcing the code in the future. To protect your private account keys, store the in a hidden file, then set them as environment variables within your virtualenv. That allows you to reference the key values as environment variables in your code, so while you maintain access, other people will not be able to appropriate your keys if you happen to put the code on Github. Make sure to list hidden files in your gitignore.

Files: twitter.py

#### Step 5: Flask Development

The point of adding a Flask app to this project is to give other people the capability to generate and tweet sentences for your bot. I used the barebone functionality of a Flask server paired with an index.html template to simply display the randomly generated sentence along with a "tweet this" button. If you're like me and not very well versed in web development, i'd definitely recommend Flask for its simplicity and straightforward customizability. It's up to you how you'd like to host your code. I went with Heroku, as they have a good amount of documentation to walk you through deploying Flask driven development.

[Tweet Generator Website](https://fast-headland-20951.herokuapp.com)

Files: Procfile, requirements.txt, runtime.txt, server.py, app.py

#### Step 6: Scripting

At this, your bot is decked out. Let's just say, a month later, you want to show it off to a couple friends. Unfortunately, no one has visited your website, and you haven't bothered tweeting in a while. This is where scripting comes in. I wrote a simple shell script that runs a python script which sends a tweet. By scheduling that shell script in your cronjob directory, you'll have a bot that tweets consistently, and your project will update itself, hands free!

Files: tweetjob.py, tweetscript.sh, output.txt
