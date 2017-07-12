import unittest
import products


class ProductTest(unittest.TestCase):

    @classmethod
    def setUpClass(ProductTest):
        ProductTest.ins = products.Product()

    def test_part_num_no_format(self):
        re = r'^[0-9]{8}$'
        self.assertRegex(ProductTest.ins.part_num(), re)


if __name__ == '__main__':
    unittest.main()
