print("Welcome to Treasure Island!")
print("Find the right path and find the treasure!")

road = input("You are at a junction with a dead end straight ahead.\n Where do you want to go? Left or Right \n").lower()



if road == "right":
    #continue in the game
    print('Good Choice! You will find a lake ahead.')
    lake = input("You have reached the lake. \n Now do you want to take the boat or do you want to swim? \n").lower()
    if lake == "wait":
        print("Great choice! you just took the boat to a house with three doors.")
        door = input("you have got three doors in front of you. Which door do you want to pick? Red, Green or Yellow \n").lower()
        if door == "red":
            print("Yay! You have found the treasure")
        elif door == "green":
            print("Ohh its a swamp full of poisonous water! you just died")
        else:
            print("YOu chose the wrong door")
    else:
        print("YOu swam into the pirahnas")

else:
    print("You fell into a ditch")

