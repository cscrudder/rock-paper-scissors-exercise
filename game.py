# RPS Game by Colton Scrudder

# Objectives:
#https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md

from random import choice
import os

def determine_winner(choice1, choice2):
    # todo: write some Python here to determine the winner
    return "TODO"

if __name__ == "__main__":
    # Print Welcome Message
    player_name = os.getenv("PLAYER_NAME", default = "Player One")
    print("------------")
    print("Welcome", player_name, "to my Rock-Paper-Scissors game...")
    print("------------")

    # Processing User Inputs
    user_move = input("Please choose 'rock', 'paper', or 'scissors': ")

    # Validating User Inputs
    if user_move.lower() == 'rock':
        user_move = 'rock'
    elif user_move.lower() == 'paper':
        user_move = 'paper'
    elif user_move.lower() == 'scissors':
        user_move = 'scissors'
    else:
        print("I did not recognize that input. Please play again!")
        exit()

    # Simulating Computer Selection
    options = ['rock','paper','scissors']
    computer_move = choice(options)

    # Determining the Winner
    if computer_move == 'rock':
        if user_move == "rock":
            result = 'tie'
        elif user_move == 'paper':
            result = 'win'
        elif user_move == 'scissors':
            result = "loss"
    elif computer_move == 'paper':
        if user_move == "rock":
            result = "loss"
        elif user_move == 'paper':
            result = 'tie'
        elif user_move == 'scissors':
            result = 'win'
    elif computer_move == 'scissors':
        if user_move == "rock":
            result = 'win'
        elif user_move == 'paper':
            result = "loss"
        elif user_move == 'scissors':
            result = 'tie'

    #Displaying Results
    print("You chose:", user_move)
    print("The computer chose:", computer_move)
    print("------------")
    if result == 'win':
        print('You won! Good work.')
    elif result == 'loss':
        print("Oh, the computer won. It's okay.")
    else:
        print("You tied. You're just as good as a computer!")
    print("------------")
    print("Thanks for playing. Please play again.")

