import unittest
from erpsy import orders
from tests.utils import RE


class OrdersTest(unittest.TestCase):

    def test_order_num_default(self):
        self.assertRegex(orders.number(), RE['default'])

    def test_orders_properties(self):
        properties = ['Order Header', 'Order Lines']
        self.assertTrue(set(orders.order().keys()) == set(properties))

    def test_order_num_style_1(self):
        self.assertRegex(orders.order(header_style='####')
                         ['Order Header'], RE[1])

    def test_order_num_line_style_3(self):
        self.assertRegex(orders.order(part_style='AA##')
                         ['Order Lines'][0]['PN'], RE[3])

    def test_orders_diff_styles(self):
        data = orders.order(header_style='AA##', part_style='####')
        self.assertRegex(data['Order Header'], RE[3])
        self.assertRegex(data['Order Lines'][0]['PN'], RE[1])

    def test_order_length(self):
        data = orders.order(line_count=3)
        self.assertEqual(3, len(data['Order Lines']))


if __name__ == '__main__':
    unittest.main()
