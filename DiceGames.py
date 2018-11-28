import numpy as np
import abc

'''
Base Classes for Die and DiceGame classes
Die shouldn't really have any children classes though because it's simple and abstract enough to initialize any die type
'''


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
    def __init__(self, numb_players):
        """
        :param numb_players: number of players except me
        :param my_bets: some data structure containing how to carry out my bets
        """
        self.__numb_players = numb_players  # number of players for the game
        self._players = dict()
        self.__dice = list()  # list of dice in the game
        self.__players_wins = dict()
        for player_numb in range(numb_players):
            self.__players_wins[player_numb] = 0

    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def prompt(self, *args):
        """
        Prompt a player for his/her strategy
        :return:
        """
        pass

    @property
    def numb_players(self):
        return self.__numb_players

    @property
    def players(self):
        return self._players

    @property
    def players_wins(self):
        return self.__players_wins
