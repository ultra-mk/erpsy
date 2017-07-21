import random as rdm
from string import ascii_uppercase, digits
from erpsy import words


def number(style=None):
    if not style:
        return str(rdm.randint(10000000, 99999999))
    else:
        return _number_style(style)


def name():
    return '{0} {1}'.format(rdm.choice(words.ADJECTIVES), rdm.choice(words.NOUNS))


def description():
    return '{0} {1}'.format(rdm.choice(words.DESCRIPTIONS), rdm.choice(words.DESCRIPTIONS))


def uom():
    return rdm.choice(words.UOMS)


def component_list(style=None, number_of_parts=1, levels=1):
    return [{'PN': number(style), 'Name': name(),
             'Desc': description(), 'Level': rdm.choice(range(1, levels + 1)),
             'QTY': rdm.choice(range(1, 9))}
            for i in range(0, number_of_parts)]


def _number_style(style):
    style = list(style)
    return ''.join([rdm.choice(digits) if i == '#' else rdm.choice(ascii_uppercase) if i == 'A' else i for i in style])
