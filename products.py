import random as rdm
from string import ascii_uppercase, digits


class Product(object):

    def __init__(self):
        pass

    def part_num(self, style=None):
        """
        Returns a part number in a user specifed style.
        If no style is given, an 8 digit part number will be returned.
        Example formats: '#' will return a digit 'A' will return a letter. 
        Any other character will return that character.
        """
        if not style:
            return str(rdm.randint(10000000, 99999999))
        else:
            return self._part_num_style(style)

    def _part_num_style(self, style):
        style = list(style)
        return ''.join([rdm.choice(digits) if i == '#' else rdm.choice(ascii_uppercase) if i == 'A' else i for i in style])
