import random
computer = random.randint(1,3) #sceglie la possa del computer prima che l'user inserisca l'input.
choices = ["Rock","Paper","Scissors"]
#---Chiediamo all'user l'input---
print("Select:\n1) Rock\n2) Paper\n3) Scissors\n")
try:
	user = int(input("(1;2;3):"))
except:
	print("\nWords aren't supported yet, numbers only (1,2,3)")
#----Convertiamo i valori----
try:
	userStr = choices[user - 1]
	computerStr = choices[computer - 1]
#---Controllo se l'utente ha inserito un numero valido e scriviamo la sua risposta---

	print(f"\nYou have choosen: {userStr}")
#----Scriviamo cosa ha messo il computer---
	print(f"\nThe computer has choosen: {computerStr}")

#----Scriviamo il vincitore---
	if user == computer:
		print("Draw!")
	elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
		print("You win!")
	else:
		print("You lost!")
except Exception as e:
	print(f"\nAn error as occured: {e}")

