import sys
from time import sleep
#Setting the size of the terminal window
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=150))

# function to make all inputs lowercase
def finput(s):
	return input(s+": ").lower()

#Function to give the player a hint if they don't know what to do
def help(choices):
	if choices == 0:
		print("Type 1 or 2")
	elif choices == 1:
		print("Where would you want to go after going to the pool? ")
	elif choices == 2:
		print("What do you do when you don't have to do anything? ")
	else:
		print("What would you do? ")
	

#Function to return True or False depending on the input
def choiceF(s):
	choiceMade = False
	while not choiceMade:
		choice = finput(s)
		if choice == "1":
			choiceMade = True
			return True
		elif choice == "2":
			choiceMade = True
			return False
		elif choice == "3":
			help(numOfChoices)
		else:
			print("Invalid Choice, Try Again.")


#Variables and Booleans 
playerLocation = "pool"
playerDidJump = False
numOfChoices = 0
date = 1
hasPracticed = False
pathsComplete = []
#The progress bar.
progressBar = "LOADING:\u001b[32m█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████            \u001b[0m"
#Game

#Printing the starting screen
print("\u001b[36m             ██╗     █████╗     ██████╗      █████╗     ██████╗     ██╗             ██╗    ██╗   ██╗    ███╗   ███╗    ██████╗     ███████╗██╗\u001b[0m")
print("\u001b[36m             ██║    ██╔══██╗    ██╔══██╗    ██╔══██╗    ██╔══██╗    ██║             ██║    ██║   ██║    ████╗ ████║    ██╔══██╗    ██╔════╝██║\u001b[0m")
print("\u001b[36m             ██║    ███████║    ██████╔╝    ███████║    ██████╔╝    ██║             ██║    ██║   ██║    ██╔████╔██║    ██████╔╝    ███████╗██║\u001b[0m ")
print("\u001b[36m        ██   ██║    ██╔══██║    ██╔══██╗    ██╔══██║    ██╔══██╗    ██║        ██   ██║    ██║   ██║    ██║╚██╔╝██║    ██╔═══╝     ╚════██║╚═╝\u001b[0m ")
print("\u001b[36m        ╚█████╔╝    ██║  ██║    ██████╔╝    ██║  ██║    ██║  ██║    ██║        ╚█████╔╝    ╚██████╔╝    ██║ ╚═╝ ██║    ██║         ███████║██╗\u001b[0m")
print("\u001b[36m         ╚════╝     ╚═╝  ╚═╝    ╚═════╝     ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝         ╚════╝      ╚═════╝     ╚═╝     ╚═╝    ╚═╝         ╚══════╝╚═╝\u001b[0m ")
print("                                                            |Type 1 for YES or 2 for NO or 3 for HELP|\u001b[0m")
print("\u001b[32m                                                    			 VVV Controls VVV.\u001b[0m")
print("""\u001b[32m
							 _______________________________________________
							|[] [] [] [] [] [] [] [] [] [] [] [] [] [] []  |
							| [ ][1][2][3][ ][ ][ ][ ][ ][ ][ ][ ][ ][   ] |
							| [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][][ ][ ]|enter||        
							| [   ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]| | |        
							| [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ] [_____] |        
							| [ ]   [ ][________________________][ ]   [ ] |        
							`----------------------------------------------'\u001b[0m""")
print("                     					You only need to use the keys shown above.")
print("                     					Type 1,2 or 3 then press enter/return ")


#Iterating through each character in the progressBar to make it look like a loading bar
for char in progressBar:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

#while loop so that the game runs until the player has completed the game
while not playerDidJump:
	#while loop for the first day of the game
	while date == 1:
		#if condition so the first choice only happens if the game has just started, used in other places with a different number of choices
		if numOfChoices == 0:
			print(" ")
			print("It was a warm summer day. Jabari and his family went to the pool.")
			print("Jabari hadn't been to the pool for sometime. He was swimming around,")
			print("when he noticed the diving board standing over the pool. He got out ")
			print("of the pool and went towards it. The diving board seemed to tower ")
			print("over him. He cautiously climed up the ladder. It was wet and Jabari ")
			print("almost fell off. When he got to the top, he looked around. He could ")
			print("see the entire pool. He looked down and saw his family they were all")
			print("smaller than him. Jabari looked down at the pool, and felt scared. He")
			print("was much higher than he thought he would be.")
			playerChoice = input("Does Jabari jump: ")
			if playerChoice == "1":
				print("Jabari jumped off the board, but he hurt himself")
				print("You completed Jabari jumps.")
				pathsComplete.append("1")
				date = 0
				playAgain = input("Do you want to play again?\n")
				if playAgain == "1":
					playerLocation = "pool"
					playerDidJump = False
					numOfChoices = 0
					date = 1
					hasPracticed = False
				else:
					exit()
			if playerChoice == "2":
				print("Jabari didn't jump")
				numOfChoices += 1
			if playerChoice == "3":
				help(numOfChoices)
		if numOfChoices == 1:
			playerChoice = choiceF("Jabari didn't jump. Does he go back home")
			if playerChoice:
				playerLocation = "home"
				numOfChoices += 1
			else:
				playerLocation = "frhome"
				numOfChoices += 1 

		if numOfChoices == 2:
			if playerLocation == "home":
				playerChoice = finput("Jabari went back home. Did he play video games")
				if playerChoice == "1":
					print("Jabari played video games at home.")
					numOfChoices += 1
					date = 2
				else:
					print("Jabari practiced jumping with his dad.")
					hasPracticed = True
					numOfChoices += 1
					date = 2

			if playerLocation == "frhome":
				playerChoice = choiceF("Jabari went to his friend's house. Did he play video games")
			if playerChoice:
				print("Jabari played video games at his friend's house.")
				numOfChoices += 1
				date = 2
			else:
				print("Jabari practiced diving into the pool at his friend's house.")
				numOfChoices += 1
				date = 2

	while date == 2:
		playerLocation = "pool"
		print("Jabari went back to the pool. He looked up at the tall diving board.")
		playerChoice = choiceF("Does Jabari go up the diving board")
		if playerChoice:
			playerChoice = choiceF("Jabari went up the diving board. Does he jump")
			if playerChoice:
				#Print statements for text in the game
				print("Jabari jumped off the diving board.")
				print("Jabari: Yay! I jumped off the diving board it was fun.")
				print("Dad: Good job! I am so proud you got over your fears. Not everyone can do what you did.")
				print("Jabari: Why not?")
				print("Dad: Some people are too scared. Others don't have a pool to play in.")
				print("Jabari: Why not?")
				print("Dad: In some places people don't have enough water to drink. Have you heard of the UN SDGs?")
				playerChoice = input("Have you heard of the SDGs? ")
				if playerChoice == "1":
				#More text
					print("Jabari: I've heard of it.")
					print("Congratulations! You have beaten Jabari Jumps. If you enjoyed the game consider learning more about UN SDG goal 9.")
					playerDidJump = True
					date = 0
					pathsComplete.append("2")
					playAgain = input("Do you want to play again?\n")
					if playAgain == "1":
						playerLocation = "pool"
						playerDidJump = False
						numOfChoices = 0
						date = 1
						hasPracticed = False
					else:
						exit()
				if playerChoice == "3":
					help(numOfChoices)
				else:
				#More text
					print("Jabari: No, I haven't. What is that?")
					print("Dad: Well, the UN wants to give everyone in the world clean water by 2030. Then everyone can jump from a diving board.")
					print("Congratulations! You have beaten Jabari Jumps. If you enjoyed the game consider learning more about UN SDG goal 9.")
					playerDidJump = True
					pathsComplete.append("3")
					date = 0
					playAgain = input("Do you want to play again?\n")
					if playAgain == "1":
						playerLocation = "pool"
						playerDidJump = False
						numOfChoices = 0
						date = 1
						hasPracticed = False
					else:
						exit()
			else:
			#More text
				print("Dad: Jabari why didn't you jump?")
				print("Jabari: I'm too scared.")
				print("Dad: Don't you know that some people don't even have water to drink!")
				print("Jabari: Why is that important.")
				print("Dad: You have the chance to do something important. You should do it. Not everyone will be able to do this.")
				print("Jabari: Okay, I'll go back and try again.")
				print("Jabari went back up the diving board. He looked down. He was really high up. But, he jumped off the diving board.")
				print("Jabari: Yay!")
				print("Congratulations! You have beaten Jabari Jumps. If you enjoyed the game consider learning more about UN SDG goal 9.")
				playerDidJump = True
				pathsComplete.append("4")
				date = 0
				playAgain = input("Do you want to play again?\n")
				if playAgain == "1":
						playerLocation = "pool"
						playerDidJump = False
						numOfChoices = 0
						date = 1
						hasPracticed = False
				else:
					exit()
		else:
			print("Jabari didn't go up the diving board.")
			date = 0
			playAgain = input("Do you want to play again?\n")
			if playAgain == "1":
				playerLocation = "pool"
				playerDidJump = False
				numOfChoices = 0
				date = 1
				hasPracticed = False
			else:
				exit()
