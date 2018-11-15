import numpy as np
import abc


class Die:
    def __init__(self, dimension, fair=True, probabilities=None):
        self.__dimension = dimension
        self.__fair = fair
        self.__probabilities = self.__determine_odds(probabilities)

    def __determine_odds(self, probabilities):
        """
        :param probabilities: custom probability if not fair, if fair it's empty
        :return:
        """
        if self.__fair:
            probabilities = list()
            p = 1/self.__dimension
            for numb in range(self.__dimension):
                probabilities.append(p)
        else:
            return probabilities
        return probabilities

    @property
    def roll(self):
        return np.random.choice(np.arange(1, self.__dimension+1), p=self.__probabilities)

    def __add__(self, another_die):
        """
        Add the sum of 2 dice rolls
        :param another_die:
        :return: return summ of 2 dice rolls
        """
        return self.roll + another_die.roll


class DiceGame(metaclass=abc.ABCMeta):
    """
    Abstract Class for DiceGame
    """
    def __init__(self, numb_players, my_bets):
        """
        :param numb_players: number of players except me
        :param my_bets: some data structure containing how to carry out my bets
        """
        self.__numb_players = numb_players  # number of players for the game
        self._players = dict()
        self.__my_bets = my_bets
        self.__dice = list()  # list of dice in the game
        self.__my_wins = 0

    @abc.abstractmethod
    def play(self):
        pass


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


