# ECON 160 - Game Theory

This folder contains miscellaneous scripts or snippets of code put together for game theory-related topics.

## Required Modules
The module [terminaltables](https://github.com/Robpol86/terminaltables) should be installed as so:
```
pip install terminaltables
```

## IDSDS.py
A quick and dirty way to run the Iterative Deletion of Strictly Dominated Strategies (IDSDS) algorithm on a simple 2-player game with numerical payoffs represented in strategic form. This is a way to solve a game when rationality of players is assumed to be common knowledge.

To input the matrix of payoffs, input an integer for the number of rows, and input each row of the matrix in order as a list of tuples (x,y), where x is the payoff for Player 1 and y is the payoff for Player 2. 

The surviving strategies are output in an ASCII table.

**Example**:

```
enter number of rows: 2

enter row of tuples (payoffs): [(10,9), (9,8)]
enter row of tuples (payoffs): [(5,3), (2,1)]

final strategies:
+---------+
| (10, 9) |
+---------+
```

## nash_equilibria.py
A (also quick and dirty) way to run the best-reply method to determine the Nash equilbrium strategies for a simple 2-player game with numerical payoffs represented in strategic form.

To input the matrix of payoffs for the players, input an integer for the number of rows, and then input a line of values separated by spaces to represent the first row of payoffs for the first player. Do this for every row for the first player, and repeat the same procedure for the second player.

The output are tuples of the payoffs that corresponding to the strategies that are Nash equilibria.

**Example**:

```
enter number of rows for each payoff matrix: 2

enter payoff row 0 for player 1: 3 2
enter payoff row 1 for player 1: 4 8

enter payoff row 0 for player 2: 3 0
enter payoff row 1 for player 2: 1 -1

nash equilibria: 
[4, 1]
```

**Disclaimer**: This code is neither very efficient nor very robust, but hey, it works.