from erpsy.parts import number


def order(header_style=None, line_count=1, part_style=None):
    return {'Order Header': number(header_style),
            'Order Lines': _lines(line_count, part_style)}


def _lines(line_count=1, part_style=None):
    return[{'PN': number(part_style)} for i in range(0, line_count)]
