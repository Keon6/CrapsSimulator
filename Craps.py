import abc
import numpy as np
from DiceGames import DiceGame, Die


class Craps(DiceGame):
    def __init__(self, numb_players=1, bet_type=1):
        super().__init__(numb_players)
        self.__dice = [Die(dimension=6), Die(dimension=6)]  # 2 fair d6
        # bet_type=1: only allow pass/don't pass bets
        # bet_type=2: allow field bets too
        # bet_type=3: allow place bets
        self.__bet_type = bet_type
        if self.__bet_type not in [1, 2, 3]:  # automatically default to some bet_type using modulus
            self.__bet_type = self.__bet_type % 3 + 1

    def __reset_bets_and_wins(self):
        for player_numb in range(self.numb_players):
            self.players_wins[player_numb] = 0
            self.players_bets[player_numb] = {
                "P": 0,  # pass
                "DP": 0,  # don't pass
                "F": 0,  # field bet
                "PL6": 0,  # place bet on 6
                "PL8": 0  # place bet on 6
            }

    def play(self):
        # At each play, reset all bets and wins
        self.__reset_bets_and_wins()
        # 1 st roll
        roll_count = 1
        print("#### NEW GAME ####")
        print(f"---- Roll {roll_count} ----")
        # Allow Player Bets
        print("Betting Time")
        for player_number in range(self.numb_players):
            print(f"Waiting for player {player_number}...")
            self.__prompt(player_number=player_number, roll_count=roll_count)

        # Roll the Dice
        on = self.__dice[0] + self.__dice[1]  # 1st roll dice sum = on
        print(f"On = {on}")

        if on in [2, 3, 12]:
            print("House Wins")
            # Allocate Wins
            for player_number in range(self.numb_players):
                self.__allocate_wins(player_number=player_number, final_roll=True, house_win=True, dice_sum=on)
            # Print Current bets and wins of all players
            print("Current Bets: ", self.players_bets, " | Current wins", self.players_wins)

        elif on in [7, 11]:
            print("Players Win")
            # Allocate Wins
            for player_number in range(self.numb_players):
                self.__allocate_wins(player_number=player_number, final_roll=True, house_win=False, dice_sum=on)
            # Print Current bets and wins of all players
            print("Current Bets: ", self.players_bets, " | Current wins", self.players_wins)

        else:
            # Allocate Wins
            for player_number in range(self.numb_players):
                self.__allocate_wins(player_number=player_number, final_roll=False, dice_sum=on)
            # Print Current bets and wins of all players
            print("Current Bets: ", self.players_bets, " | Current wins", self.players_wins)
            # Continue Rolling Otherwise
            dice_sum = 0
            while dice_sum not in [7, on]:  # Continue Rolling until game ends
                # Update number of rolls
                roll_count += 1
                print(f"---- Roll {roll_count} ----")
                # Allow Player Bets
                for player_number in range(self.numb_players):
                    self.__prompt(player_number=player_number, roll_count=roll_count)

                # Roll Dice and take sum
                dice_sum = self.__dice[0] + self.__dice[1]
                print(f"Dice Sum = {dice_sum}")
                if dice_sum != (7 or on):
                    # Allocate Wins
                    for player_number in range(self.numb_players):
                        self.__allocate_wins(player_number=player_number, final_roll=False, dice_sum=dice_sum)
                    # Print Current bets and wins of all players
                    print("Current Bets: ", self.players_bets, " | Current wins", self.players_wins)

            if dice_sum == on:  # On rolled again => Players Win
                print("Players Win")
                # Allocate Wins
                for player_number in range(self.numb_players):
                    self.__allocate_wins(player_number=player_number, final_roll=True, house_win=False, dice_sum=on)
                # Print Current bets and wins of all players
                print("Current Bets: ", self.players_bets, " | Current wins", self.players_wins)

            elif dice_sum == 7:  # 7 rolled => House Wins
                print("House Wins")
                # Allocate Wins
                for player_number in range(self.numb_players):
                    self.__allocate_wins(player_number=player_number, final_roll=True, house_win=True, dice_sum=7)
                # Print Current bets and wins of all players
                print("Current Bets: ", self.players_bets, " | Current wins", self.players_wins)

        return self.players_wins

    def __prompt(self, player_number, roll_count):
        # ROLL 1
        if roll_count == 1:
            if input("Press p to pass, d to not pass") == 'p':
                print("Pass Bet")
                self.players_bets[player_number]["P"] = int(input("How much do you wanna bet?"))
            else:
                print("Don't Pass Bet")
                self.players_bets[player_number]["DP"] = int(input("How much do you wanna bet?"))
        # Any Rolls
        if self.__bet_type == 1:
            pass
            # Can't change Pass/Don't Pass Bets
        elif self.__bet_type == 2:
            print("Field Bet")
            self.players_bets[player_number]["F"] = int(input("Field Bet Amount?"))

        elif self.__bet_type == 3:
            print("Field Bet")
            self.players_bets[player_number]["F"] = int(input("Field Bet Amount?"))
            print("Place Bets")
            self.players_bets[player_number]["PL6"] = int(input("How much on 6?"))
            self.players_bets[player_number]["PL8"] = int(input("How much on 8?"))

    def __allocate_wins(self, player_number, final_roll, dice_sum, house_win=None):
        """
        Allocate or take wins depending on player's performance
        :return:
        """
        # Take care of field bets
        if dice_sum in [2, 12]:  # 2x on field
            self.players_wins[player_number] += 2*self.players_bets[player_number]["F"]
        elif dice_sum in [3, 4, 9, 10, 11]:  # 1x on field
            self.players_wins[player_number] += self.players_bets[player_number]["F"]
        elif dice_sum == 5:  # lose on field
            self.players_wins[player_number] += -self.players_bets[player_number]["F"]
        elif dice_sum == 6:  # lose on field, 1X on PL6
            self.players_wins[player_number] += \
                (-self.players_bets[player_number]["F"] + self.players_bets[player_number]["PL6"])
        elif dice_sum == 8:  # lose on field, 1x on PL8
            self.players_wins[player_number] += \
                (-self.players_bets[player_number]["F"] + self.players_bets[player_number]["PL8"])

        # Last roll, also take care of pass/don't pass bets
        if final_roll:
            if house_win:
                self.players_wins[player_number] += \
                    (self.players_bets[player_number]["DP"]-self.players_bets[player_number]["P"]
                     - self.players_bets[player_number]["PL6"] - self.players_bets[player_number]["PL8"])
            else:
                self.players_wins[player_number] += \
                    (self.players_bets[player_number]["P"] - self.players_bets[player_number]["DP"])
