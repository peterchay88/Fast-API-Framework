from wonderwords import RandomSentence
import random

random_sentence = RandomSentence()


def generate_random_sentence():
    """
    This function generates a simple random sentence
    :return:
    """
    sentence = random_sentence.bare_bone_sentence()
    return sentence


def generate_random_number(minimum=0, maximum=100):
    """
    This function generates a random number between the specified range. Default is 0 to 100.
    :return:
    """
    random_number = random.randint(minimum, maximum)
    return random_number
