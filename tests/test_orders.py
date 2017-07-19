import unittest
from erpsy import orders

RE = {'default': r'^[0-9]{8}$'}


class OrdersTest(unittest.TestCase):

    def test_order_num_default(self):
        self.assertRegex(orders.number(), RE['default'])


if __name__ == '__main__':
    unittest.main()
