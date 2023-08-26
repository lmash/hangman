import random


class Hangman:
    """
    This class is used to represent a Hangman game.

    Attributes:
        word_list (list): a list of words.
        num_lives (int): the number of lives a player has at the start of the game. Defaults to 5.
    """
    def __init__(self, word_list, num_lives=5):
        """See help(Hangman) for accurate signature"""
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))  # Number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        This function is used to check if a guess is in the word.

        Args:
            guess (str): the guessed letter.
        """
        guess_lower = guess.lower()

        if guess_lower in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter.lower() == guess_lower:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    @staticmethod
    def _valid_guess(guess):
        return len(guess) == 1 and guess.isalpha()

    def ask_for_input(self):
        """This function is used to ask a user to guess a letter and validates the guess."""
        while True:
            guess = input("Enter a single letter: ")

            if not self._valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


if __name__ == "__main__":
    x = Hangman(word_list=["apPle", "pEar", "Cherry", "Blackcurrant", "mangO"])
    x.ask_for_input()
