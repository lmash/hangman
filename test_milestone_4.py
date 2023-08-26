from milestone_4 import Hangman


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
