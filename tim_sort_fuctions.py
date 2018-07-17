# Functions to support the example 06: Using tim sort to ordenate objects
# generate_string: build a string with aleatory letters
# generate_number: return a random number in a interval between 0 and the number of your choice

import random
import string


def generate_string(size):
    return ''.join(random.choice(string.ascii_letters) for i in range(size))


def generate_number(range):
    return random.randint(0, range)
