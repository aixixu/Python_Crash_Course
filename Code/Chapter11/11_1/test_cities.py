import unittest
from city_functions import countryandcity

class CityandCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        CityandCountry_name = countryandcity('santiago','chile')
        self.assertEqual(CityandCountry_name,'Santiago, Chile')

if __name__ == 'main':
    unittest.main()