# CrapsSimulator
Python program that simulates a game of craps, helps you judge your betting strategy, optimize expected return/loss or minimize variance of your return/losses.

You can use this simulation like you are playing an actual game of Craps.

### Files
#### DiceGames.py:
Contains class representing a Die and an abstract base class for any DiceGame

#### Craps.py: 
This is the real deal. Contains a Craps class, that takes 1) number of palayers 2) betting type as parameters

bet_type=1 -> Only bet on Pass or Don't Pass

bet_type=2 -> Only bet on Pass or Don't Pass & Field Bet

bet_type=3 -> Only bet on Pass or Don't Pass & Field Bat & Place Bets on 6 and 8

#### Tests.py: 
Just a testing script to make sure the simulation works as intended

### User Manual
You can use this simulation like you are actually playing a real game of craps. You can even play with your friends if you'd like.
Just run it in a command line with no arguments. It will prompt you to enter inputs for bets.

When prompted to "pass or not pass", type 'p' to pass or 'd' to not pass.

## Why?
This is a simulation I made for fun, but it might be useful for general purposes for both degenerate or occaisional gamblers.

## What?
I will run some non linear optimization to Maximize:

Utility Function defined as: 
E[W] - c*Var(W)
Or in words, the expected profit minus penalty given by variance of profit, wehre c is a parameter on how much to penalize the variance.

## How?
I will run some simulations to test the betting strategy outputted by the optimization and how well it does.

## Why should you care?
Disclaimer:
I am not guaranteeing any successful Craps betting strategy. In fact, all casino games including Craps, are designed in favor of the Casino, not the players. I am taking a probabilistic approach to see what betting strategy has the best expected profit or has the least chance of losing money (or some combination of both).

I'm not liable for you losing money.

Please be careful!

## What Else?
I think the design patterns I used are pretty bad. If I have time, I'll probably use some kind of factory pattern to pump out simulations with different betting constraitns.

I also might want to write all this in C++ eventually just because.
