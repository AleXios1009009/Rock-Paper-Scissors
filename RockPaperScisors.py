import random
computer = random.randint(1,3) #sceglie la possa del computer prima che l'user inserisca l'input.

#---Chiediamo all'user l'input---
print("Select:\n1) Rock\n2) Paper\n3) Scissors\n")
try:
	user = int(input("(1;2;3):"))
except:
	print("\nWords aren't supported yet, numbers only (1,2,3)")
#----Convertiamo i valori----
#User
try:
	if user == 1: userStr = "Rock"
	if user == 2: userStr = "Paper"
	if user == 3: userStr = "Scissors"

#computer
	if computer == 1: computerStr = "Rock"
	if computer == 2: computerStr = "Paper"
	if computer == 3: computerStr = "Scissors"

#---Controllo se l'utente ha inserito un numero valido e scriviamo la sua risposta---
	if (user <4) and (user >=1):
		print(f"\nYou have choosen: {userStr}")
	else:
		print("choose a valid number (1,2,3)")
		quit()
#----Scriviamo cosa ha messo il computer---
	print(f"\nThe computer has choosen: {computerStr}")

#----Scriviamo il vincitore---
	if user == computer:
		print("Draw!")
	elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
		print("You win!")
	else:
		print("Better luck next time!")
except:
	print("\nAn error as occured")

