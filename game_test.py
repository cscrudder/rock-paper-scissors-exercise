# This file allows pytest to run a test to make sure the "game.py" file works correctly.

# https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/challenges.md


# import determine_winner custom function from "game.py"
from game import determine_winner

# new function that uses syntax from pytest to test if "game.py" is working correctly
def test_determination_of_the_winner():

    assert determine_winner("rock", "rock") == None
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None
