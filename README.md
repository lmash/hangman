# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

### Prerequisites

Hangman requires python

### Installation

Clone the repo

```sh
git clone https://github.com/lmash/hangman.git
```

### Usage

1. Change to the hangman folder

```sh
cd hangman
```

2. Run the following from the command line

```sh
python hangman.py
```

### Rules

- Guess one letter at a time.
- Any letter A-Z or a-z is valid.
- A correctly guessed letter will be displayed in the console.
- If you correctly guess all the letters in the word you win!
- You have 5 lives, after 5 incorrect guesses you lose.

### Description of files

Non-Python files:

| filename  | description                                             |
| --------- | ------------------------------------------------------- |
| README.md | Text file (markdown format) description of the project. |

Python modules:

| filename            | description                                                                  |
| ------------------- | ---------------------------------------------------------------------------- |
| milestone_2.py      | Create variables for the game                                                |
| milestone_3.py      | Functions to ask for input and check if the guessed character is in the word |
| milestone_4.py      | A Hangman game class. Has methods to ask for input and check a guess         |
| test_milestone_4.py | Unit tests for Hangman class initialization and methods                      |

### Running tests
Install pytest
```sh
pip install pytest
```

Run tests
```sh
pytest
```