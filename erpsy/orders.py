from erpsy.parts import number
from erpsy import words
import random as rdm


def order(header_style=None, line_count=1, part_style=None):
    return {'Order Header': number(header_style),
            'Order Lines': _lines(line_count, part_style)}


def _lines(line_count=1, part_style=None):
    return[{'PN': number(part_style)} for i in range(0, line_count)]


def _inco_terms():
    return rdm.choice(words.INCOTERMS)


def _currency(default=None):
    if default == None:
        return rdm.choice(words.CURRENCY)
    else:
        return default


def _payment_terms(default=None):
    if default == None:
        return rdm.choice(words.PAYMENT)
    else:
        return default
