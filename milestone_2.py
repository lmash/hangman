import random
from string import ascii_letters


word_list = ['apple', 'pear', 'cherry', 'blackcurrant', 'mango']
print(f"Entire list: {word_list}")

word = random.choice(word_list)
print(f"Selected word: {word}")

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess in ascii_letters:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

