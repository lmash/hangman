# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

### Installation

Pre-requisite: Conda/miniconda installed

1. Clone the repo

```sh
git clone https://github.com/lmash/hangman.git
```

2. Change to the hangman folder

```sh
cd hangman
```

3. Create the conda env and install required packages

```shell
conda env create -f environment.yml
```

### Usage

Run the following from the command line

```sh
python milestone_5.py
```

### Rules

- Guess one letter at a time.
- Any letter A-Z or a-z is valid.
- A correctly guessed letter will be displayed in the console with the word
- If you correctly guess all the letters in the word you win!
- You have 5 lives, after 5 incorrect guesses you lose.

### File structure

```
├── LICENSE
├── README.md
├── environment.yml
├── milestone_2.py
├── milestone_3.py
├── milestone_4.py
├── milestone_5.py
└── test_milestone_5.py
```

### Description of files

Non-Python files:

| filename         | description                                             |
| ---------------- | ------------------------------------------------------- |
| README.md        | Text file (markdown format) description of the project. |
| environment.yaml | Text file (yaml format) Conda environment file          |

Python modules:

| filename            | description                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| milestone_2.py      | Create variables for the game                                                       |
| milestone_3.py      | Functions to ask for input and check if the guessed character is in the word        |
| milestone_4.py      | A Hangman game class. Has methods to ask for input and check a guess                |
| milestone_5.py      | Hangman game. Contains hangman class with game methods and a method to run the game |
| test_milestone_5.py | Unit tests for Hangman game                                                         |

### Run tests

```sh
cd <path_to_hangman>
pytest --verbose
```

### License

Licensed under the [GPL-3.0](https://github.com/lmash/hangman/blob/main/LICENSE) license.
