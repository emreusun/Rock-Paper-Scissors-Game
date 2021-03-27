# Import packages to extend Python (just like we extend Sublime, Atom, or VSCode)
from random import randint 
# re-import our game variables
from gameComponents import gameVars, winLose

# [] => this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold mutiple items.
# arrays are indexed (their contents are assigned a number)
# the index always starts at 0
   		 	

# player_choice == False
while gameVars.player_choice is False:
	print("==============*/ RPS GAME */==============")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("===========================================")
	# Version 1, to explain array indexing
	# player_choice = choices [1]
	# print("index 1 in the choice array is" + player_choice + ",which is paper")

	print("Choose your weapon! Or type quit to exit\n")

	gameVars.player_choice = input("Choose rock, paper, or scissors: \n")
	#player_choice now equals TRUE -> it has a values

	if gameVars.player_choice == "quit":
		print("You chose to quit")
		exit()

	gameVars.computer_choice = gameVars.choices[randint(0, 2)]


	print("user chose: "  + gameVars.player_choice)

	# this will be the AI choice -> a random pick from the choices array 

	print("computer chose:"  + gameVars.computer_choice)

	if gameVars.computer_choice == gameVars.player_choice:
		print("tie")

	elif gameVars.computer_choice == "rock":	
		if gameVars.player_choice == "scissors":
			
			#verbose way 
			#player_lives = player_lives - 1
			#simplified way
			gameVars.player_lives -= 1
			print("you lose! player lives:", gameVars.player_lives)
		else:
		    print("you win!")
		    gameVars.computer_lives -= 1

	elif gameVars.computer_choice == "paper":	
		if gameVars.player_choice == "rock":
			gameVars.computer_lives -= 1
			print("you lose! player lives:", gameVars.player_lives)
		   
		else:
		    print("you win!")	
		    gameVars.player_lives -= 1

	elif gameVars.computer_choice == "scissors":	
		if gameVars.player_choice == "paper":
			gameVars.player_lives -= 1
			print("you lose! player lives:", gameVars.player_lives)
		else:
		    print("you win!")	
		    gameVars.computer_lives -= 1
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")
		
	if gameVars.computer_lives == 0:
		winLose.winorlose("won")
	else:
		gameVars.player_choice = False
		


	print("Player lives:", gameVars.player_lives)
	print("Computer lives:", gameVars.computer_lives)

	# map the loop keep running, by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True
	gameVars.player_choice = False






