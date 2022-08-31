'''
A two player game of rock, paper, scissors.
'''

import time

moves = {10:"Rock", 20:"Paper", 30:"Scissors"}

print("\nRock Paper Scissors! 2 players.\n\nCodes for each move:\nRock: 1\nPaper: 2\nScissors: 3\n")

def game(player1_input, player2_input):
    '''
    Rock 1
    Paper 2
    Scissors 3

    Take two inputs
    Divide one by the other to obtain a quotient
    Compare them against a dictionary
    with precalculated results from
    the equation that correlate
    to a win or loose for each player.
    '''

    win_loose_dictionary = { # Dictionary where different quotients correspond to different results
        3:1, 20:1, 15:1,
        30:2, 6:2, 5:2,
        10:0
    }

    if not isinstance(player1_input, int) or not isinstance(player2_input, int):
        return 3 # Return 3 if input not an integer

    # Obtain quotient.
    # Multiplied by ten so that when converted to integer the second significant figure is not lost
    quotient = int(10 * (int(player1_input) / int(player2_input))) 
    return win_loose_dictionary[quotient]

p1 = input("Player 1, enter your move: ")
p2 = input("Player 2, enter your move: ")

if game(p1, p2) == 1:
    print("Player 1 wins!")
elif game(p1, p2) == 2:
    print("Player 2 wins!")
elif game(p1, p2) == 3:
    print("Invalid Entry!")
else:
    print("Draw!")

time.sleep(5)

