import pytest
from typing import List

from milestone_5 import Hangman


@pytest.fixture(autouse=True)
def default_game():
    # Code that will run before your test
    game = Hangman(word_list=["apple"])
    yield game
    # Code that will run after your test


def test_hangman_class_attributes_initialized():
    """
    Hangman class initialization attributes
    word is set to the computer selected word converted to lowercase
    num_letters is set to unique letters
    num_lives defaults to 5
    word_list is set to the word list argument
    list_of_guesses is set to an empty list
    word_guessed is set to a list of 5 underscores
    """
    game = Hangman(word_list=["apPle"])
    assert game.word == 'apple'
    assert game.num_letters == 4
    assert game.num_lives == 5
    assert game.word_list == ["apPle"]
    assert game.list_of_guesses == []
    assert game.word_guessed == ['_', '_', '_', '_', '_']


def test_hangman_class_num_lives():
    """Hangman class num_lives defaults is set to the num_lives argument"""
    game = Hangman(word_list=["apPle"], num_lives=10)
    assert game.num_lives == 10


def test_lowercase_letter_in_word():
    """Method check_guess updates attributes num_letters and word_guessed when letter found in word"""
    game = Hangman(word_list=["apPle"])
    game.check_guess('p')
    assert game.num_letters == 3
    assert game.word_guessed == ['_', 'p', 'p', '_', '_']


def test_uppercase_letter_in_word():
    """Method check_guess updates attributes num_letters and word_guessed when uppercase letter found in word"""
    game = Hangman(word_list=["apPle"])
    game.check_guess('P')
    assert game.num_letters == 3
    assert game.word_guessed == ['_', 'P', 'P', '_', '_']


def test_consecutive_correct_guesses():
    """Method check_guess updates attributes for consecutive correct guesses"""
    game = Hangman(word_list=["apPle"])
    game.check_guess('P')
    game.check_guess('l')
    game.check_guess('e')
    assert game.num_letters == 1
    assert game.word_guessed == ['_', 'P', 'P', 'l', 'e']


def test_letter_not_in_word():
    """Method check_guess updates attribute num_lives when letter not found in word"""
    game = Hangman(word_list=["apPle"])
    game.check_guess('z')
    assert game.num_lives == 4


def test_game_won(default_game):
    """Method won returns True if number of lives > 0 and there are no letters left to guess"""
    default_game.num_lives = 1
    default_game.num_letters = 0
    assert default_game.won() is True
    assert default_game.lost() is False


def test_game_lost(default_game):
    """Method lost returns True if number of lives = 0"""
    default_game = Hangman(word_list=["apple"])
    default_game.num_lives = 0
    assert default_game.lost() is True
    assert default_game.won() is False


def test_display_word_guessed(default_game):
    """Method __str__ returns a string representation of word_guessed"""
    assert str(default_game) == '_____'


def get_console_output(capsys) -> List:
    """This functions captures stdout & stderr from the console and returns a list of the output"""
    captured = capsys.readouterr()  # capsys allows capture of stdout & stderr
    return captured.out.split('\n')


def test_more_than_one_letter_entered(monkeypatch, capsys, default_game):
    """Method ask_for_input requests additional input when more than one letter entered"""
    inputs = iter(['ab', 'b'])  # define multiple inputs to be monkeypatched
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    default_game.ask_for_input()
    outputs = get_console_output(capsys)
    assert outputs[0] == 'Invalid letter. Please, enter a single alphabetical character.'


def test_invalid_letter_entered(monkeypatch, capsys, default_game):
    """Method ask_for_input requests additional input when an invalid letter is entered"""
    inputs = iter(['7', 'b'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    default_game.ask_for_input()
    outputs = get_console_output(capsys)
    assert outputs[0] == 'Invalid letter. Please, enter a single alphabetical character.'
