import random as rdm
from string import ascii_uppercase, digits


def number(style=None):
    if not style:
        return str(rdm.randint(10000000, 99999999))
    else:
        return _number_style(style)


def name():
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


def description():
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


def uom():
    uoms = ('Each', 'Batch', 'Case', 'Unit')
    return rdm.choice(uoms)


def component_list(style=None, number_of_parts=1, levels=1):
    return [{'PN': number(style), 'Name': name(),
             'Desc': description(), 'Level': rdm.choice(range(1, levels + 1)),
             'QTY': rdm.choice(range(1, 9))}
            for i in range(0, number_of_parts)]


def _number_style(style):
    style = list(style)
    return ''.join([rdm.choice(digits) if i == '#' else rdm.choice(ascii_uppercase) if i == 'A' else i for i in style])
