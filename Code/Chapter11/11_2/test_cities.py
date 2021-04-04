import unittest
from city_functions import countryandcity

class CityandCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        CityandCountry_name = countryandcity('santiago','chile')
        self.assertEqual(CityandCountry_name,'Santiago, Chile')
    def test_city_country_population(self):
        CityandCountry_name = countryandcity('santiago','chile',population=5000000)
        self.assertEqual(CityandCountry_name,'Santiago, Chile 5000000')
        
if __name__ == 'main':
    unittest.main()