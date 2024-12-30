import random
from hangman_art import stages, logo
word_list = ["kaaley", "good", "luck"]

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over and lives != 0:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess} ")

    display = ""
    for letter in chosen_word:        
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left")
        if lives == 0:
            game_over = True
            print("Youw lose.")


    if "_" not in display :
        print("You Win!")
        game_over = True

    print(stages[lives])
