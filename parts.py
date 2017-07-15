import random as rdm
from string import ascii_uppercase, digits


class Part(object):

    def __init__(self):
        pass

    def number(self, style=None):
        """
        Returns a part number in a user specifed style.
        If no style is given, an 8 digit part number will be returned.
        Example formats: '#' will return a digit 'A' will return a letter. 
        Any other character will return that character.
        """
        if not style:
            return str(rdm.randint(10000000, 99999999))
        else:
            return self._number_style(style)

    def name(self):
        nouns = ('Resistor', 'Potentiometer', 'Capacitor',
                 'Inductor', 'Oscillator', 'Relay', 'Transformer', 'Battery', 'Integrated Circuit',
                 'Display', 'Condenser', 'Reactor', 'Isolator', 'Control Knob', 'PWB', 'Diode',
                 'Thermistor', 'CMOS', 'Timer', 'Comparator', 'Regulator', 'Aplifier', 'Cerebra', 'Cerebro')

        adjectives = ('Active', 'Arc', 'DC', 'Fused', 'Passive',
                      'Electromechanical', 'Constant Current', 'MOSFET', 'Incandescent',
                      'Diode', 'MIS', 'Piezoelectrical', 'Choke', 'Solenoid', 'Selenium',
                      'Distributed', 'Voltage Regulation', 'Light Emitting', 'Variable Capacitance',
                      'Carbon Film', 'Metal Film', 'Variable', 'CDS', 'NTC', 'PTC', 'CTR', 'Electrolytic',
                      'Tantalum', 'Ceramic', 'Multilayer', 'Polystyrene', 'Polypropylene', 'Mica', 'Repulsing')

        return '{0} {1}'.format(rdm.choice(adjectives), rdm.choice(nouns))

    def _number_style(self, style):
        style = list(style)
        return ''.join([rdm.choice(digits) if i == '#' else rdm.choice(ascii_uppercase) if i == 'A' else i for i in style])
