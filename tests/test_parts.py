import unittest
from erpsy import parts
from tests.utils import RE


class PartsTest(unittest.TestCase):

    def test_part_num_default(self):
        self.assertRegex(parts.number(), RE['default'])

    def test_part_num_style_1(self):
        self.assertRegex(parts.number(style='####'), RE[1])

    def test_part_num_style_2(self):
        self.assertRegex(parts.number(style='#######'), RE[2])

    def test_part_num_style_3(self):
        self.assertRegex(parts.number(style='AA##'), RE[3])

    def test_str_types(self):
        properties = [parts.name(), parts.description(), parts.uom(),
                      parts.component_list()[0]['Name'],
                      parts.component_list()[0]['Desc']]
        self.assertTrue(all(isinstance(x, str) for x in properties))

    def test_int_types(self):
        properties = [parts.component_list()[0]['Level'],
                      parts.component_list()[0]['QTY'], ]
        self.assertTrue(all(isinstance(x, int) for x in properties))

    def test_bom_components(self):
        self.assertEqual(1, len(parts.component_list()))

    def test_bom_components_55(self):
        self.assertEqual(55, len(parts.component_list(number_of_parts=55)))

    def test_component_properties(self):
        properties = ['PN', 'Name', 'Desc', 'Level', 'QTY']
        self.assertTrue(set(parts.component_list()[0]) == set(properties))


if __name__ == '__main__':
    unittest.main()
