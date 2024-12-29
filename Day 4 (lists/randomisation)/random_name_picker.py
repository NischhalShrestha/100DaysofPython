import random

friends = ["risab", "anish", "Rushan", "Andrew"]

will_pay = random.choice(friends)

print(will_pay + " will pay the bill")

#2ND OPTION
random_index = random.randint(0,3)
print(friends[random_index])

