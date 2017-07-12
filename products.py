import random
from string import ascii_uppercase, digits


class Product(object):

    def __init__(self):
        pass

    def part_num(self, format=None):
        """
        Returns a part number in a user specifed format.
        If no format is given, an 8 digit part number will be returned.
        """
        if not format:
            return str(random.randint(10000000, 99999999))
