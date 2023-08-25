import random
from string import ascii_letters


def guess_valid(guess: str) -> bool:
    """
    Validates user guess. A valid guess has a length of 1 and
    is a upper or lowercase letter

    Args:
        guess (str): User guess
    Returns:
        True if guess valid, False if guess invalid
    """
    if len(guess) == 1 and guess in ascii_letters:
        print("Good guess!")
        return True

    print("Oops! That is not a valid input.")
    return False


word_list = ["apple", "pear", "cherry", "blackcurrant", "mango"]
print(f"Entire list: {word_list}")

word = random.choice(word_list)
print(f"Selected word: {word}")

guess = input("Enter a single letter: ")
guess_valid(guess)
