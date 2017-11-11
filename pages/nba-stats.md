title: 2017 NBA Hackathon Application
date: 2017-11-08
tags: [Basketball, Python]
description: Will the 2018 Warriors ever lose? And what did the 2017 final regular season standings look like?

Since 2016, the National Basketball Association began hosting an annual [NBA Hackathon](https://hackathon.nba.com/)! As a basketball aficionado and computer science student, I think sports analytics is an exciting Wild West part of the growing trend of information driven decision making. This past year, I submitted an application for the NBA application. As a part of the application, I had to design and compute answers for two different questions. Both were interesting brain teasers, and I thought I'd share my approaches to these problems in this post!

##### Q1: Probability of a Losing Streak
**Prompt**: Calculate the probability that the 2016-2017 Warriors will lose consecutive game. Assume that the probability the Warriors win a game is fixed at 80%.

**Introduction**<br>
Before approaching the problem, there are a couple numbers required for contextualization. We assume that there are a total of 82 games in the NBA’s regular season. Given that there is a fixed 80% chance the Warriors win a single game, there would subsequently be a 20% chance they lose a game. The probability that the Warriors lose two games in a row would be (0.20)2 = 0.04 or 4% chance of losing two games in a row. However, this number by itself would not be enough to estimate the cumulative probability for two reasons:

1. The number of consecutive loses is not limited to two. Given n games and k losses, there are 'n choose k' ordered ways for the season of n games to
k play out with k losses and n - k wins.

2. Given a fixed number of losses, there is a specific probability associated with each quantity of losses.

From these observations, this problem can be modeled as a binomial distribution. By definition, the binomial distribution is the discrete probability distribution of the number of successes given n consecutive experiments with a binary set of outcomes. The parameters n and p would respectively be the number of games and the probability of winning.

**Computation**<br>
The formula for calculating the probability of a binomial distribution can be logically arrived upon. To calculate the probability of exactly k successes in n trials, the formula is:

<img src="/static/pictures/2017NBAHack/BinomialFormula.png" alt="Drawing" style="height: 40px;"/>

With this formula, assuming that a ”success” is a loss and ”p” would be the probability of losing, we could calculate the probability losing k games given all possible orders of losing those games out of 82. However, in this question, we’re focusing on consecutive games.

An alternative approach would be to count the number of win-lose sequences that would not lead to two consecutive losses. Given 82 total games and k losses, there would be '83-k choose k' configurations that avoid consecutive losses. The logic starts with the assumption that given k losses, each loss must be followed by a win except the last game. From k - 1 losses, there would be 2k - 2 guaranteed games from above. There is one single game reflecting the final loss, and then 82 - (2k - 2) - 1 = 83 - 2k unassigned wins. Therefore, in total, there are (k - 1) + 1 + (83 - 2k) = 83 - k ”loss containing units” that we can choose losses from. In other words, '83-k choose k' choices.

Given the number of choices, we can apply the probability formula above as the following:

<img src="/static/pictures/2017NBAHack/BinomialFormula2.png" alt="Drawing" style="height: 40px;"/>

We would need to calculate all probabilities of k losses from 0 to 41 losses (given that more than 41 losses would guarantee consecutive losses). Therefore, we could take the summation of probabilities across these range of losses. The final equation would be the following:

<img src="/static/pictures/2017NBAHack/BinomialFormula3.png" alt="Drawing" style="height: 40px;"/>

As we can see, there is a 5.88% chance that the Warriors do not lose consecutive games. Therefore, I would conclude that it is *highly unlikely the Warriors will not lose consecutive games during the regular season*.

##### Q2: Probability of a Losing Streak
**Prompt**: 
