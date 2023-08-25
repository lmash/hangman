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

### How to play

You will be asked to guess a single letter. Any letter A-Z or a-z will be accepted.

"Enter a single letter:"

- If the guessed letter matches a letter in the word ...

- If the guessed letter does no match a letter in the word ...

- You have x guesses

### Description of files

Non-Python files:

| filename  | description                                             |
| --------- | ------------------------------------------------------- |
| README.md | Text file (markdown format) description of the project. |

Python modules:

| filename       | description                                                                  |
| -------------- | ---------------------------------------------------------------------------- |
| milestone_2.py | Create variables for the game                                                |
| milestone_3.py | Functions to ask for input and check if the guessed character is in the word |
