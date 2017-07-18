import random as rdm
from string import ascii_uppercase, digits


class Part(object):

    def __init__(self):
        pass

    def number(self, style=None):
        if not style:
            return str(rdm.randint(10000000, 99999999))
        else:
            return self._number_style(style)

    def name(self):
        nouns = ('Resistor', 'Potentiometer', 'Capacitor',
                 'Inductor', 'Oscillator', 'Relay', 'Transformer', 'Battery', 'Integrated Circuit',
                 'Display', 'Condenser', 'Reactor', 'Isolator', 'Control Knob', 'PWB', 'Diode',
                 'Thermistor', 'CMOS', 'Timer', 'Comparator', 'Regulator', 'Amplifier', 'Cerebra', 'Cerebro')

        adjectives = ('Active', 'Arc', 'DC', 'Fused', 'Passive',
                      'Electromechanical', 'Constant Current', 'MOSFET', 'Incandescent',
                      'Diode', 'MIS', 'Piezoelectrical', 'Choke', 'Solenoid', 'Selenium',
                      'Distributed', 'Voltage Regulation', 'Light Emitting', 'Variable Capacitance',
                      'Carbon Film', 'Metal Film', 'Variable', 'CDS', 'NTC', 'PTC', 'CTR', 'Electrolytic',
                      'Tantalum', 'Ceramic', 'Multilayer', 'Polystyrene', 'Polypropylene', 'Mica', 'Repulsing')

        return '{0} {1}'.format(rdm.choice(adjectives), rdm.choice(nouns))

    def description(self):
        descriptions = ('FLIP-FLOP, 2 CIRCUITS', 'Logic IC Case Style',
                        'PDIP', 'No. of Pins: 14', 'Case Style: PDIP', 'Single Transmitter/Receiver',
                        'RS-422/RS-485', '8-Pin PDIP Tube', 'XOR Gate', '4-Element', '2-IN Bipolar',
                        '14-Pin PDIP,XOR Gate', '4-Element 2-IN', 'Bipolar 14-Pin', 'PDIP XOR Gate',
                        'IBUS', 'JIS', 'DC Block Type', 'Electrical Coil Sensor', 'Type 76553', 'Fiber Optic Circuit',
                        'Constant Input Resistance', 'Constant Output resistance', 'TI', 'Stark Industries Model',
                        'Reed Richards Design', 'Later Design Type', 'Reference 22320f', 'Von Doom Captive Design',
                        'McCoy Style Conversion', 'Cho Model', 'Log Counter Implementatoon', 'MK VI', 'MKVII',
                        'MacTaggert Implementation', 'Pym Particle Reduction', 'Bannertech')

        return '{0} {1}'.format(rdm.choice(descriptions), rdm.choice(descriptions))

    def uom(self):
        uoms = ('Each', 'Batch', 'Case', 'Unit')
        return rdm.choice(uoms)

    def _number_style(self, style):
        style = list(style)
        return ''.join([rdm.choice(digits) if i == '#' else rdm.choice(ascii_uppercase) if i == 'A' else i for i in style])


class BOM(Part):

    def __init__(self, number_of_parts=0, depth=1):
        self.number_of_parts = number_of_parts
        self.depth = depth

    def number(self, style=None):
        return Part.number(self, style)

    def components(self, style=None):
        return [{'PN': Part.number(style), 'Name': Part.name(self),
                 'Desc': Part.description(self), 'Level': rdm.choice(range(1, self.depth + 1)),
                 'QTY': rdm.choice(range(1, 9))}
                for i in range(0, self.number_of_parts)]

    def name(self):
        nouns = ('Gentech', 'McCoy', 'Test', 'Motor')
        adjectives = ('Kit', 'Assy', 'Assembly')
        return "{0} {1}".format(nouns, adjectives)
