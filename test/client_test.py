import unittest
from client import getDataPoint, getRatio


class TestGetDataPoint(unittest.TestCase):

    def test_get_data_point(self):
        quote = {
            'stock': 'ABC',
            'top_bid': {'price': '10'},
            'top_ask': {'price': '12'}
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 10.0)
        self.assertEqual(ask_price, 12.0)
        self.assertEqual(price, 11.0)


class TestGetRatio(unittest.TestCase):

    def test_get_ratio(self):
        self.assertEqual(getRatio(10, 5), 2.0)
        self.assertEqual(getRatio(10, 0), None)
