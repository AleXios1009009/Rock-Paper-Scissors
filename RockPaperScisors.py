import random
user = int(input("Select:\n1) Rock\n2) Paper\n3) Scissors\n(1;2;3): "))
if user <4:
	if user >= 1:
		print(f"Hai selezionato la risposta : {user}")
	else:
		print("Don't cheat")
		quit()
else:
	print("Don't cheat")
	quit()
computer = random.randint(1,3)
#----Scriviamo cosa ha messo il computer---
if computer == 1:
	print(f"The computer choose: Rock!")
elif computer == 2:
	print(f"The computer choose: Paper!")
elif computer == 3:
	print(f"The computer choose: Scissors!")
else:
	print("Great! you broke my script, GG")
#----Scriviamo il vincitore---
if user == computer:
	print("Draw!")
elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
	print("You win!")
else:
	print("Better luck next time!")

