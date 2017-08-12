import unittest
from erpsy import orders
from erpsy import words
from tests.utils import RE


class OrdersTest(unittest.TestCase):

    def test_order(self):
        properties = set(['order number', 'incoterms',
                          'currency', 'payment terms', 'lines'])
        self.assertEqual(properties, set(orders.order().keys()))

    def test_lines(self):
        properties = set(['part number', 'quantity', 'price'])
        self.assertEqual(properties, set(orders.lines()[0].keys()))

    def test_line_len_default(self):
        self.assertEqual(1, len(orders.order()['lines']))

    def test_line_len(self):
        self.assertEqual(10, len(orders.order(line_count=10)['lines']))
    # def test_order_num_default(self):
    #     self.assertRegex(orders.number(), RE['default'])

    # def test_orders_properties(self):
    #     properties = ['Order Header', 'Order Lines']
    #     self.assertTrue(set(orders.order().keys()) == set(properties))

    # def test_order_num_style_1(self):
    #     self.assertRegex(orders.order(header_style='####')
    #                      ['Order Header'], RE[1])

    # def test_order_num_line_style_3(self):
    #     self.assertRegex(orders.order(part_style='AA##')
    #                      ['Order Lines'][0]['PN'], RE[3])

    # def test_orders_diff_styles(self):
    #     data = orders.order(header_style='AA##', part_style='####')
    #     self.assertRegex(data['Order Header'], RE[3])
    #     self.assertRegex(data['Order Lines'][0]['PN'], RE[1])

    # def test_order_length(self):
    #     data = orders.order(line_count=3)
    #     self.assertEqual(3, len(data['Order Lines']))

    # def test_order_inco_terms(self):
    #     self.assertRegex(orders._inco_terms(), RE['INCOTERMS'])

    # def test_order_currency(self):
    #     self.assertRegex(orders._currency(), RE['INCOTERMS'])

    # def test_order_currency_default(self):
    #     self.assertEqual('USD', orders._currency(default='USD'))

    # def test_order_payment_terms(self):
    #     self.assertIn(orders._payment_terms(), words.PAYMENT)

if __name__ == '__main__':
    unittest.main()
