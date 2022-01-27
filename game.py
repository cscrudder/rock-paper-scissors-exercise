# RPS Game by Colton Scrudder

# Objectives:
#https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md

# import modules needed
from random import choice
import os

#function to determine winner that also works with pytest
def determine_winner(user_move, computer_move):
    if computer_move == 'rock':
        if user_move == "rock":
            result = None
        elif user_move == 'paper':
            result = 'paper'
        elif user_move == 'scissors':
            result = 'rock'
    elif computer_move == 'paper':
        if user_move == "rock":
            result = "paper"
        elif user_move == 'paper':
            result = None
        elif user_move == 'scissors':
            result = 'scissors'
    elif computer_move == 'scissors':
        if user_move == "rock":
            result = 'rock'
        elif user_move == 'paper':
            result = "scissors"
        elif user_move == 'scissors':
            result = None
    return result

#if statement needed ensure user is running the correct file
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

    # Determining the winning move by using custom function
    winning_move = determine_winner(user_move, computer_move)

    #determines if the user won, lost, or tied based on the winning move
    if winning_move == user_move:
        result = 'win'
    elif winning_move == computer_move:
        result = 'loss'
    else: 
        result = "tie"

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
    print("Thanks for playing. Please play again.\n")

