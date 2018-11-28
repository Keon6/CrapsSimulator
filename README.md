# CrapsSimulator
Python program that simulates a game of craps, helps you judge your betting strategy, optimize expected return/loss or minimize variance of your return/losses.

## Why?
This is for a algorithms for non-linear optimization class, but it might be useful for general purposes for both degenerate or occaisional gamblers.

## What?
I will run some non linear optimization to Maximize:

Utility Function defined as: 
E[W] - c*Var(W)
Or in words, the expected profit minus penalty given by variance of profit, wehre c is a parameter on how much to penalize the variance.

## How?
I will run some simulations to test the betting strategy outputted by the optimization and how well it does.

## Why should you care?
Disclaimer first, I am not guaranteeing any successful Craps betting strategy. In fact, all casino games, including Craps, are designed to in favor of the Casino, not the players.
I am taking a probabilistic approach and see what betting strategy has the best expected profit or has the least chance of losing money.
Please be careful! 

I'm not liable for you losing money.


## What Else?
I might want to write all this in C++ eventually just cuz.
