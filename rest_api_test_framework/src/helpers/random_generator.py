import wonderwords
from wonderwords import RandomSentence, random_word
import random

random_sentence = RandomSentence()


def generate_random_sentence(char_length=0):
    """
    This function generates a simple random sentence
    :return:
    """
    if char_length > 0:
        sentence = random_sentence.bare_bone_sentence()
        while True:
            if len(sentence) < char_length:
                extra_words = random_sentence.bare_bone_sentence()
                sentence = f"{sentence} {extra_words}"
                continue
            elif len(sentence) >= char_length:
                break
    elif char_length == 0:
        sentence = random_sentence.bare_bone_sentence()
    return sentence


def generate_random_word():
    """
    This function generates a random word
    :return:
    """
    word = wonderwords.RandomWord()
    return word.word()


def generate_random_number(minimum=0, maximum=100):
    """
    This function generates a random number between the specified range. Default is 0 to 100.
    :return:
    """
    random_number = random.randint(minimum, maximum)
    return random_number
