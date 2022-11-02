# 24/01/2022
import os
import time

def store_guess(guess):
    with open("guesses.txt", "a") as file:
        file.write(guess)


def guess_coded(secret):
    coded = ""
    with open("guesses.txt", "r") as file:
        guesses = file.read()

    for i in secret:
        if i == " ":
            coded += "   "
        elif i in guesses:
            coded += i + " "
        else:
            coded += "_ "

    return coded


def guess_clean(secret):
    coded = ""
    with open("guesses.txt", "r") as file:
        guesses = file.read()

    for i in secret:
        if i == " ":
            coded += " "
        elif i in guesses:
            coded += i
        else:
            coded += "_"

    return coded


def has_won(secret):
    guess = guess_clean(secret)
    if secret == guess:
        return True

    return False


def hangman(lives):
    if lives == 6:
        hangman = ("    ╔===╗\n"
                   "    ∥   ∥\n"
                   "        ∥\n"
                   "        ∥\n"
                   "        ∥\n"
                   "        ∥\n"
                   " [======╝\n"
                   )

        return hangman

    elif lives == 5:
        hangman = ("    ╔===╗\n"
                   "    ∥   ∥\n"
                   "    O   ∥\n"
                   "        ∥\n"
                   "        ∥\n"
                   "        ∥\n"
                   " [======╝\n"
                   )

        return hangman

    elif lives == 4:
        hangman = ("    ╔===╗\n"
                   "    ∥   ∥\n"
                   "    O   ∥\n"
                   "    │   ∥\n"
                   "    │   ∥\n"
                   "        ∥\n"
                   " [======╝\n"
                   )

        return hangman

    elif lives == 3:
        hangman = ("    ╔===╗\n"
                   "    ∥   ∥\n"
                   "    O   ∥\n"
                   "   /│   ∥\n"
                   "    │   ∥\n"
                   "        ∥\n"
                   " [======╝\n"
                   )

        return hangman

    elif lives == 2:
        hangman = ("    ╔===╗\n"
                   "    ∥   ∥\n"
                   "    O   ∥\n"
                   "   /│\  ∥\n"
                   "    │   ∥\n"
                   "        ∥\n"
                   " [======╝\n"
                   )

        return hangman

    elif lives == 1:
        hangman = ("    ╔===╗\n"
                   "    ∥   ∥\n"
                   "    O   ∥\n"
                   "   /│\  ∥\n"
                   "    │   ∥\n"
                   "   /    ∥\n"
                   " [======╝\n"
                   )

        return hangman

    elif lives == 0:
        hangman = ("    ╔===╗\n"
                   "    ∥   ∥\n"
                   "    O   ∥\n"
                   "   /│\  ∥\n"
                   "    │   ∥\n"
                   "   / \  ∥\n"
                   " [======╝\n"
                   )

        return hangman


def guess_is_valid(secret, guess):
    with open("guesses.txt", "r") as file:
        guesses = file.read()

    if len(guess) > 1:
        return False, "Guess Only One Letter!"
    if guess == "" or guess == " ":
        return False, "Please Type a Guess!"
    if guess in guesses:
        return False, "Already Guessed!"

    return True, 1


def guess_is_correct(secret, guess):
    if guess in secret:
        return True

    return False


lives = 6
secret_wrd = input("Input Secret Word: ")
os.system("cls")

with open("guesses.txt", "w") as file:
    pass


while lives > 0 and not has_won(secret_wrd):
    print(hangman(lives))

    print(guess_coded(secret_wrd))

    with open("guesses.txt", "r") as file:
        data = file.read()

    print("Guesses:")
    for index, val in enumerate(data):
        if len(data) == 1:
            print(val)
        else:
            if index != len(data) - 1:
                print(val + ", ", end="")
            else:
                print(val)

    guess = input("\nInput guess: ")
    guess.lower()

    valid, valid_error = guess_is_valid(secret_wrd, guess)
    if valid:
        store_guess(guess)
        if guess_is_correct(secret_wrd, guess):
            print("Correct!")
        else:
            print("Incorrect!")
            lives -= 1
    else:
        print(valid_error)

    time.sleep(1)
    os.system("cls")

if lives < 1:
    print(hangman(0))
    print(f"\nThe Word was: {secret_wrd}")
    print("YOU LOSE!")
if has_won(secret_wrd):
    print(f"The Word was: {secret_wrd}")
    print("\nYOU WIN!")

