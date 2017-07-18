import unittest
import parts

RE = {'default': r'^[0-9]{8}$',
      '1': r'^[0-9]{4}$',
      '2': r'^[0-9]{7}$',
      '3': r'^[A-Z]{2}[0-9]{2}$'}


class PartTest(unittest.TestCase):

    @classmethod
    def setUpClass(PartTest):
        PartTest.data = parts.Part()

    def test_part_num_default(self):
        self.assertRegex(PartTest.data.number(), RE['default'])

    def test_part_num_style_1(self):
        self.assertRegex(PartTest.data.number(style='####'), RE['1'])

    def test_part_num_style_2(self):
        self.assertRegex(PartTest.data.number(style='#######'), RE['2'])

    def test_part_num_style_3(self):
        self.assertRegex(PartTest.data.number(style='AA##'), RE['3'])

    def test_name(self):
        self.assertTrue(isinstance(PartTest.data.name(), str))

    def test_name_len(self):
        self.assertTrue(1 < len(PartTest.data.name()) < 100)

    def test_description(self):
        self.assertTrue(isinstance(PartTest.data.description(), str))

    def test_description_len(self):
        self.assertTrue(1 < len(PartTest.data.description()) < 100)

    def test_uom(self):
        self.assertTrue(isinstance(PartTest.data.uom(), str))


class BOMTest(unittest.TestCase):

    @classmethod
    def setUpClass(BOMTest):
        BOMTest.data = parts.BOM()

    def test_bom_num_default(self):
        self.assertRegex(BOMTest.data.number(), RE['default'])

    def test_bom_num_style1(self):
        self.assertRegex(BOMTest.data.number(style='####'), RE['1'])

    def test_part_num_style_2(self):
        self.assertRegex(BOMTest.data.number(style='#######'), RE['2'])

    def test_bom_style_3(self):
        self.assertRegex(BOMTest.data.number(style='AA##'), RE['3'])

    def test_bom_components(self):
        bom = parts.BOM(number_of_parts=1)
        self.assertEqual(1, len(bom.components()))

    def test_bom_components_type(self):
        bom = parts.BOM(number_of_parts=1)
        self.assertRegex(bom.components()[0]['PN'], RE['default'])

    def test_bom_components_55(self):
        bom = parts.BOM(number_of_parts=55)
        self.assertEqual(55, len(bom.components()))

    def test_bom_components_type_55(self):
        bom = parts.BOM(number_of_parts=55)
        self.assertRegex(bom.components()[-1]['PN'], RE['default'])

    def test_bom_name(self):
        self.assertTrue(isinstance(BOMTest.data.name(), str))

    def test_component_name(self):
        bom = parts.BOM(number_of_parts=55)
        self.assertTrue(isinstance(bom.components()[0]['Name'], str))

    def test_component_desc(self):
        bom = parts.BOM(number_of_parts=55)
        self.assertTrue(isinstance(bom.components()[0]['Desc'], str))

    def test_component_depth(self):
        bom = parts.BOM(number_of_parts=55)
        self.assertTrue(isinstance(bom.components()[0]['Level'], int))

    def test_component_QTY(self):
        bom = parts.BOM(number_of_parts=55)
        self.assertTrue(isinstance(bom.components()[0]['QTY'], int))

if __name__ == '__main__':
    unittest.main()
