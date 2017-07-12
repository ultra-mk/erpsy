import unittest
import products


class ProductTest(unittest.TestCase):

    def test_part_num_no_format(self):
        part = products.Product()
        re = r'^[0-9]{8}$'
        self.assertRegex(part.part_num(), re)

    def test_part_num_style_1(self):
        part = products.Product()
        re = r'^[0-9]{4}$'
        self.assertRegex(part.part_num(style='####'), re)

    def test_part_num_style_2(self):
        part = products.Product()
        re = r'^[0-9]{7}$'
        self.assertRegex(part.part_num(style='#######'), re)

    def test_part_num_style_3(self):
        part = products.Product()
        re = r'^[A-Z]{2}[0-9]{2}$'
        self.assertRegex(part.part_num(style='AA##'), re)


if __name__ == '__main__':
    unittest.main()
