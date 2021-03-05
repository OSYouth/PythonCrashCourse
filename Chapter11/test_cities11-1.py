import unittest
from city_functions import get_city_country

class TestCityCountry(unittest.TestCase):
    '''测试city_functions'''

    def test_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

unittest.main()