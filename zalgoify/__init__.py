import random

__version__ = '0.1.0'

characters = list(range(65056, 65072))

def zalgoify(text, zalgos):
    retstr = ""
    for char in text:
        retchar = char
        for _ in range(5):
            retchar += chr(random.choice(characters))
        retstr += retchar
    return retstr