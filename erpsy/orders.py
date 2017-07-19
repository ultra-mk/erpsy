from erpsy.parts import number


def order(header_style=None, number_of_lines=1, part_style=None):
    order_header = number(header_style)
    return {'Order Header': order_header, 'Order Lines': [{'PN': number(part_style)}]}


# def _lines()
