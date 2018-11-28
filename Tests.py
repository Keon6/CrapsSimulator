from Craps import Craps


# Test Craps Simulation code
def test(numb_players, bet_type):
    """
    Unit Test for just pass and don't pass Bets
    :return:
    """
    print(f"########## TESTING | Bet_Type={bet_type} & Number_of_Players={numb_players} ##########")
    game = Craps(numb_players=numb_players, bet_type=bet_type)
    print("Final Wins: ", game.play())


if __name__ == "__main__":
    for n in range(1,6):
        test(numb_players=n, bet_type=1)
        test(numb_players=n, bet_type=2)
        test(numb_players=n, bet_type=3)
