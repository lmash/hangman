import random
from typing import List


class Hangman:
    """
    This class is used to represent a Hangman game.

    Attributes:
        word_list (list): a list of words.
        num_lives (int): the number of lives a player has at the start of the game. Defaults to 5.
    """
    def __init__(self, word_list: List, num_lives: int = 5):
        """See help(Hangman) for accurate signature"""
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))  # Number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess: str):
        """
        This function is used to check if a guess is in the word.

        Args:
            guess (str): the guessed letter.
        """
        # Change to lowercase for check to see if in word, as word is converted to lowercase
        guess_lower = guess.lower()

        if guess_lower in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess_lower:
                    # guess is added to word_guessed and displayed to the user in the case entered
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    @staticmethod
    def _valid_guess(guess: str) -> bool:
        return len(guess) == 1 and guess.isalpha()

    def ask_for_input(self):
        """This function is used to ask a user to guess a letter and validate the guess."""
        while True:
            guess = input("Enter a single letter: ")

            if not self._valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess.lower())
                break

    def won(self) -> bool:
        """This function returns True if the game has been won"""
        return self.num_lives > 0 and not self.num_letters > 0

    def lost(self) -> bool:
        """This function returns True if the game has been lost"""
        return self.num_lives == 0

    def __str__(self) -> str:
        """This function returns a string representation of correctly guessed letters in the word"""
        return "".join(self.word_guessed)


def play_game(word_list: List):
    """
    This functions runs the game. It checks to see whether the user needs to enter another letter or has won/lost

    Args:
        word_list (list): A list of words for the hangman game
    """
    game = Hangman(word_list=word_list, num_lives=5)

    while True:
        if game.won():
            print("Congratulations. You won the game!")
            print(f"Word is: {game}")
            break
        elif game.lost():
            print("You lost!")
            break
        else:
            print(f"{'*' * 80}\nWord to guess is: {game}")
            game.ask_for_input()


if __name__ == '__main__':
    play_game(word_list=['mango', 'blackcurrant', 'Apple', 'pEar', 'Cherry'])
