print("Welcome to the Pthon Pizza Delivery Services!")
size = input("What size pizza do you want? S M or L : \n")
pepperoni = input('Do you want pepperoni on your pizza? Y or N : \n')
extra_cheese = input("do you want extra cheese? Y or N: \n")
to_pay = 0

#to work out 
if size == "S":
    to_pay += 15

elif size == "M":
    to_pay = 20

elif size == "L":
    to_pay = 25

else:
    print("No pizza selected.")

if pepperoni == "Y":
    if size == "S":
        to_pay += 2
    else:
        to_pay += 3

if extra_cheese == "Y":
    to_pay += 1

print(f"You have to pay : {to_pay}")


