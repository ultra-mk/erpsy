from erpsy.parts import number
from erpsy import words
import random as rdm


def order(header_style=None, line_count=1):
    order = {'order number': number(header_style), 'incoterms': rdm.choice(words.INCOTERMS),
             'currency': rdm.choice(words.CURRENCY), 'payment terms': rdm.choice(words.PAYMENT)}
    order['lines'] = lines(line_count)
    return order


def lines(line_count=1, part_style=None):
    return[{'part number': number(part_style), 'quantity': rdm.randint(1, 50),
            'price': rdm.uniform(2.5, 250.0)}
           for i in range(0, line_count)]
