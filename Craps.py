import abc
import numpy as np
from DiceGames import DiceGame, Die


class Craps(DiceGame):
    def __init__(self, numb_players, my_bets):
        super().__init__(numb_players, my_bets)
        self.__dice = [Die(dimension=6), Die(dimension=6)]  # 2 fair d6

    def play(self):
        # TODO: How to implement??
        # 1 st roll
        roll_count = 1
        print(f"Roll {roll_count}")
        sum = self.__dice[0] + self.__dice[1]
        if sum == (2 or 3 or 12):
            print("House Wins")
            return self.__my_wins
        elif sum == (7 or 11):
            print("Players Win")
            return self.__my_wins
        else:
            roll_count += 1
            print(f"Roll {roll_count}")