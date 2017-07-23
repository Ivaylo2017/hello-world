'''
This is the code for "Rock, Scissors, Paper" game for 2 players
Each player must enter either rock, scissors or paper (supposedly without seeing each other's input)
The winner is determined according to the rules:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
'''
'''
Create a flag variable called msg with initial value 'y' which is to allow the game to run until a player
enters 'n' for no when asked 'Would you like to play again?'
Then input is stored as lower case and evaluated against tuple of pre-defined permitted input values.
if values are same we have draw. Since computer doesn't understand words but numbers I compare the positions
of those words in the list - 0, 1 and 2.The tuple is ordered so that power increases from left to right with the only exception
that the first element beats the last one. 
'''
def game():
	msg ='y'
	val = ('scissors', 'rock', 'paper')
	while msg != 'n':
		pl1 = input("Player 1 please enter rock, scissors or paper: ").lower()
		pl2 = input("Player 2 please enter rock, scissors or paper: ").lower()
		if pl1 in val and pl2 in val:
			'''
			With 3^2 = 9 we have 9 possible combinations 3 of which end up in draw
			We then only have to provision for 6 scenarios.
			'''
			if pl1 == pl2:
				print("Draw!")
			'''
			If player1's element index is equal to player2's + 1. player 1 wins. Same will happen if player1's element is 0 and player2 
			element is 2. That's the exception.
			'''
			elif val.index(pl1) == val.index(pl2)+1 or val.index(pl2) == val.index(pl1) + 2:
				print("Player 1 wins!!!")
			else:                                # In any other case player 2 will be the winner
				print("Player 2 wins!!!")
		else:                                     #This else statement captures any cases when input is not what is expected
			print("Players please spell words as shown. Resetting...")
		msg = input("Would you like to play again? y for 'Yes' and n for 'No':")
	print("Thank you for playing! Exiting...")      #When user says No, we'll print Thank you message and exit  

game()