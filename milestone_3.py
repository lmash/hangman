import random

word_list = ["apple", "pear", "cherry", "blackcurrant", "mango"]
word = random.choice(word_list)


def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            break

        print("Invalid letter. Please, enter a single alphabetical character.")    

    check_guess(guess)


def check_guess(guess):
    guess_lower = guess.lower()
    if guess_lower in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word.")


ask_for_input()
