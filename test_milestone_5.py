import pytest
from typing import List

import milestone_5
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
    """Method ask_for_input prints failure message and requests additional input when more than one letter input"""
    inputs = iter(['ab', 'b'])  # define multiple inputs to be monkeypatched
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    default_game.ask_for_input()
    outputs = get_console_output(capsys)
    assert outputs[0] == 'Invalid letter. Please, enter a single alphabetical character.'


def test_invalid_letter_entered(monkeypatch, capsys, default_game):
    """Method ask_for_input prints failure message and requests additional input when an invalid letter is input"""
    inputs = iter(['7', 'b'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    default_game.ask_for_input()
    outputs = get_console_output(capsys)
    assert outputs[0] == 'Invalid letter. Please, enter a single alphabetical character.'


def test_valid_letter_entered(monkeypatch, capsys, default_game):
    """Method ask_for_input prints success message when valid letter input"""
    monkeypatch.setattr('builtins.input', lambda _: 'a')
    default_game.ask_for_input()
    outputs = get_console_output(capsys)
    assert outputs[0] == 'Good guess! a is in the word.'
    assert default_game.list_of_guesses == ['a']


def test_duplicate_valid_letter_entered(monkeypatch, capsys, default_game):
    """Method ask_for_input prints message and requests additional input when a previously entered letter is input"""
    monkeypatch.setattr('builtins.input', lambda _: 'a')
    default_game.ask_for_input()
    get_console_output(capsys)
    # Enter 'a' again followed by 'b' (Need 2 entries as valid entry needed to break out of input loop)
    inputs = iter(['a', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    default_game.ask_for_input()
    outputs = get_console_output(capsys)
    assert outputs[0] == 'You already tried that letter!'


def test_message_when_game_won(monkeypatch, capsys):
    """Method play_game prints message when the game has been won"""
    inputs = iter(['y', 'r', 'e', 'C', 'h'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    milestone_5.play_game(['Cherry'])
    outputs = get_console_output(capsys)
    assert outputs[len(outputs) - 3] == 'Congratulations. You won the game!'
    assert outputs[len(outputs) - 2] == 'Word is: Cherry'


def test_message_when_game_lost(monkeypatch, capsys):
    """Method play_game prints message when the game has been lost"""
    inputs = iter(['z', 'w', 'o', 'a', 'm'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    milestone_5.play_game(['Cherry'])
    outputs = get_console_output(capsys)
    assert outputs[len(outputs) - 2] == 'You lost!'
