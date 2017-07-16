import unittest
import parts


class PartTest(unittest.TestCase):

    def test_part_num_no_format(self):
        part = parts.Part()
        re = r'^[0-9]{8}$'
        self.assertRegex(part.number(), re)

    def test_part_num_style_1(self):
        part = parts.Part()
        re = r'^[0-9]{4}$'
        self.assertRegex(part.number(style='####'), re)

    def test_part_num_style_2(self):
        part = parts.Part()
        re = r'^[0-9]{7}$'
        self.assertRegex(part.number(style='#######'), re)

    def test_part_num_style_3(self):
        part = parts.Part()
        re = r'^[A-Z]{2}[0-9]{2}$'
        self.assertRegex(part.number(style='AA##'), re)

    def test_name(self):
        part = parts.Part()
        self.assertEqual(True, isinstance(part.name(), str))

    def test_name_len(self):
        part = parts.Part()
        self.assertTrue(1 < len(part.name()) < 100)

    def test_description(self):
        part = parts.Part()
        self.assertEqual(True, isinstance(part.description(), str))

    def test_description_len(self):
        part = parts.Part()
        self.assertTrue(1 < len(part.description()) < 100)


class BOMTest(unittest.TestCase):

    def test_bom_no_format(self):
        bom = parts.BOM()
        re = r'^[0-9]{8}$'
        self.assertRegex(bom.number(), re)

    def test_bom_components(self):
        bom = parts.BOM(number_of_parts=1)
        self.assertEqual(1, len(bom.components()))

    def test_bom_components_type(self):
        bom = parts.BOM(number_of_parts=1)
        self.assertEqual('Stuff', bom.components())

    def test_bom_components_55(self):
        bom = parts.BOM(number_of_parts=55)
        self.assertEqual(55, len(bom.components()))

    # def test_bom_components_type_55(self):
    #     bom = parts.BOM(number_of_parts=55)
    #     self.assertEqual('Stuff', bom.components())


if __name__ == '__main__':
    unittest.main()
