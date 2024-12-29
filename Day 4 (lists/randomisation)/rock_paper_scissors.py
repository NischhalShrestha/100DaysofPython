import random

choose = ["rock", "paper", "Scissors"]

user_choice = int(input("Choose one: \n 0 for rock, 1 for paper and 2 for scissors"))

#option 1 (MAile aafaile gareko yo chai)
if user_choice == 0:
    print ("you chose: " + choose[0])
    computer_choice = random.choice(choose)
    print("the computer chose: " + computer_choice)
    if computer_choice == choose[user_choice]:
        print ("Its a draw")
    elif computer_choice == choose[1]:
        print ("the computee won")
    else:
        print ("You win!")

elif user_choice == 1:
    print("You have choosen: " + choose[1])
    computer_choice = random.choice(choose)
    print("The computer has choosen: " + computer_choice)
    if computer_choice == choose[user_choice]:
        print ("Its a draw")
    elif computer_choice == choose[0]:
        print ("You win!")
    else :
        print ("the computee won")

elif user_choice == 2:
    print("You have choosen: " + choose[2])
    computer_choice = random.choice(choose)
    print("The computer has choosen: " + computer_choice)
    if computer_choice == choose[user_choice]:
        print ("Its a draw")
    elif computer_choice == [0]:
        print ("the computee won")
    else:
        print ("You Won!")

#option 2 (Yo chai ideal)
choose = ["Rock", "Paper", "Scissors"]
#Gets user input and validates it
user_choice = int(input("Choose one: \n0 for rock, 1 for paper and 2 for scissors: \n"))

if user_choice in [0, 1, 2]:
    print("You chose: " + choose[user_choice])
    computer_choice = random.choice(choose)
    print("The computer chose: " + computer_choice)

    # To determine the winner
    if choose[user_choice] == computer_choice:
        print("It's a draw!")
    elif (user_choice == choose[0] and computer_choice == "scissors") or \
         (user_choice == choose[1] and computer_choice == "rock") or \
         (user_choice == choose[2] and computer_choice == "paper"):
        print("You win!")
    else:
        print("The computer won!")
else:
    print("Invalid choice. Please choose 0, 1, or 2.")
