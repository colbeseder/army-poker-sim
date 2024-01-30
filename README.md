Army Poker Sim
==============

In the army in 2023, we played a game that we (incorrectly) call "_Chinese Poker_".

During those games, several questions arose. This project aims to anser those questions, by simulating larget numbers of random games.

Questions
---------

1. How much does luck play a factor? (vs ideal strategy)
2. Is it better to focus on grouping, or flush/straight?
3. Is a _flush_ unfairly weighted?

Answers (preliminary)
---------------------

    1. How much does luck play a factor?

We see that the current top strategy  beats _chooseLeft_ (basically random) over 95% of the time. So strategy clearly matters.

But once if we include only players with even trivial strategy, they lose less than 64% against the current best players. So even a good player will lose roughly one third of all games, to a somewhat competent opponent.

    1. Is it better to focus on grouping, or flush/straight?

At this stage, it seems that prioritising groupings (eg. pairs, three of a kind, etc) is a better strategy. Even players who completely ignore opportunities for flush or straight beat _preferFlushStraightGroup_

This may change as more advanced strategies take more notice of which cards are still in the deck.

    3. Is a _flush_ unfairly weighted?

This remains an open question

Raw Results
-----------
[Jupyter Notebook](tournament.ipynb)

Next Steps
----------

We should create more advanced strategies, that:

1. Consider the opponent's board state
2. account for which cards remain in the deck

Adding new strategies is easy. At a file to the _src/strategies_ directory, that includes a "choose" function.

Then run the _tournament_ notebook to see how it compares.
