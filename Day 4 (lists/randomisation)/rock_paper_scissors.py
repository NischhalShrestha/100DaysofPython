import random
choose = ["rock", "paper", "Scissors"]

user_choice = input("Choose one \n 0 for rock, 1 for paper and 2 for scissors")

if user_choice == 0:
    print ("you chose: " + choose[0])
    computer_choice = random.choice(choose)
    print("the computer chose: " + computer_choice)
    if computer_choice == user_choice:
        print ("Its a draw")
    elif computer_choice == choose[1]:
        print ("the computee won")
    else:
        print ("You win!")

elif user_choice == 1:
    print("You have choosen: " + choose[1])
    computer_choice = random.choice(choose)
    print("The computer has choosen: " + computer_choice)
    if computer_choice == [user_choice]:
        print ("Its a draw")
    elif computer_choice == choose[0]:
        print ("You win!")
    else :
        print ("the computee won")

elif user_choice == 2:
    print("You have choosen: " + choose[2])
    computer_choice = random.choice(choose)
    print("The computer has choosen: " + computer_choice)
    if computer_choice == [user_choice]:
        print ("Its a draw")
    elif computer_choice == [0]:
        print ("the computee won")
    else:
        print ("You Won!")



