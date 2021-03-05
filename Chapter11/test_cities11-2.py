import unittest
from city_country_population_fuctions import get_city_country_population

class TestCityCountry(unittest.TestCase):
    '''测试city_functions'''

    def test_city_country(self):
        city_country = get_city_country_population('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        ccp = get_city_country_population('santiago', 'chile', population='5000000')
        self.assertEqual(ccp, 'Santiago, Chile - population 5000000')

unittest.main()