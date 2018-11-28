import abc
import numpy as np
from DiceGames import DiceGame, Die
import keyboard


# TODO: how to manage bets??????
class Craps(DiceGame):
    def __init__(self, numb_players=1, bet_type=1):
        super().__init__(numb_players)
        self.__dice = [Die(dimension=6), Die(dimension=6)]  # 2 fair d6
        # bet_type=1: only allow pass/don't pass bets
        # bet_type=2: allow field bets too
        # bet_type=3: allow place bets
        self.__bet_type = bet_type
        if self.__bet_type != (1 or 2 or 3): # automatically default to some bet_type using modulus
            self.__bet_type = self.__bet_type % 3 + 1

    def play(self):
        # TODO: How to change wins?

        # 1 st roll
        roll_count = 1
        print("#### NEW GAME ####")
        print(f"---- Roll {roll_count} ----")
        # Allow Player Bets
        print("Betting Time")
        for player_number in range(self.numb_players):
            print(f"Waiting for player {player_number}...")
            self.prompt(player_number=player_number, roll_count=roll_count)

        # Roll the Dice
        on = self.__dice[0] + self.__dice[1]  # 1st roll dice sum = on
        print(f"On = {on}")
        if on == (2 or 3 or 12):
            print("House Wins")
            return self.players_wins
        elif on == (7 or 11):
            print("Players Win")
            return self.players_wins

        # Continue Rolling Otherwise
        dice_sum = 0
        while dice_sum != (7 or on):  # Continue Rolling until game ends
            # Update number of rolls
            roll_count += 1
            print(f"---- Roll {roll_count} ----")
            # Allow Player Bets
            for player_number in range(self.numb_players):
                self.prompt(player_number=player_number, roll_count=roll_count)
            # Roll Dice and take sum
            dice_sum = self.__dice[0] + self.__dice[1]
            print(f"Dice Sum = {dice_sum}")
            if dice_sum == on:  # On rolled again => Players Win
                print("Players Win")
                return self.players_wins
            elif dice_sum == 7:  # 7 rolled => House Wins
                print("House Wins")
                return self.players_wins

    def prompt(self, player_number, roll_count):
        if roll_count == 1:
            if input("Press p to pass, d to not pass") == 'p':
                print("Pass Bet")
                return 1
            else:
                print("Don't Pass Bet")
                return 0
        if self.__bet_type == 1:
            pass  # Can't change Pass/Don't Pass Bets
        elif self.__bet_type == 2:
            # TODO: prompt for field bets
            pass
        elif self.__bet_type == 3:
            # TODO: prompt for field and place bets
            pass
