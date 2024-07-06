import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_data_points = [
      ('ABC', 120.48, 121.2, 120.84),
      ('DEF', 117.87, 121.68, 119.77)
    ]
    for i, quote in enumerate(quotes):
        data_point = getDataPoint(quote)
        self.assertEqual(data_point, expected_data_points[i], f"Failed for quote {quote}")

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_data_points = [
      ('ABC', 120.48, 119.2, 119.84),
      ('DEF', 117.87, 121.68, 119.77)
    ]
    for i, quote in enumerate(quotes):
        data_point = getDataPoint(quote)
        self.assertEqual(data_point, expected_data_points[i], f"Failed for quote {quote}")

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_emptyQuote(self):
      quote = {'top_ask': {'price': 0.0, 'size': 0}, 'timestamp': '', 'top_bid': {'price': 0.0, 'size': 0}, 'id': '',
             'stock': ''}
      expected_data_point = ('', 0.0, 0.0, 0.0)
      data_point = getDataPoint(quote)
      self.assertEqual(data_point, expected_data_point, "Price should be 0.0 for empty quote")


  def test_getDataPoint_noBid(self):
    quote = {'top_ask': {'price': 120.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': None,
           'id': '0.109974697771', 'stock': 'ABC'}
    expected_data_point = ('ABC', 0.0, 120.0, 60.0)
    data_point = getDataPoint(quote)
    self.assertEqual(data_point, expected_data_point, "Price should be equal to ask price when there is no bid")


  def test_getDataPoint_noAsk(self):
      quote = {'top_ask': None, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.0, 'size': 36},
           'id': '0.109974697771', 'stock': 'ABC'}
      expected_data_point = ('ABC', 120.0, 0.0, 60.0)
      data_point = getDataPoint(quote)
      self.assertEqual(data_point, expected_data_point, "Price should be equal to bid price when there is no ask")


  def test_getRatio_valid(self):
      price_a = 120.0
      price_b = 100.0
      expected_ratio = 1.2
      ratio = getRatio(price_a, price_b)
      self.assertEqual(ratio, expected_ratio, "Ratio should be 1.2")


  def test_getRatio_zeroPriceB(self):
      price_a = 120.0
      price_b = 0.0
      expected_ratio = None  # Assuming the function returns None or raises an error for division by zero
      ratio = getRatio(price_a, price_b)
      self.assertIsNone(ratio, "Ratio should be None when price_b is 0")


  def test_getRatio_zeroPriceA(self):
      price_a = 0.0
      price_b = 100.0
      expected_ratio = 0.0
      ratio = getRatio(price_a, price_b)
      self.assertEqual(ratio, expected_ratio, "Ratio should be 0.0 when price_a is 0")


  def test_getRatio_bothZeroPrices(self):
      price_a = 0.0
      price_b = 0.0
      expected_ratio = None  # Assuming the function returns None or raises an error for division by zero
      ratio = getRatio(price_a, price_b)
      self.assertIsNone(ratio, "Ratio should be None when both prices are 0")

if __name__ == '__main__':
    unittest.main()
