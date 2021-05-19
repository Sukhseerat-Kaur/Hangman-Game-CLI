import random

def load_words():
    word_list = open("words.txt").read().split()
    return word_list


def choose_word():
    """
    word_list (list): list of words (strings)
    this function return one random world from list
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
