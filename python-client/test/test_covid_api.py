"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.nina.api.covid_api import CovidApi  # noqa: E501

from deutschland import nina


class TestCovidApi(unittest.TestCase):
    """CovidApi unit test stubs"""

    def setUp(self):
        self.api = CovidApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_ags_covid_rules(self):
        """Test case for get_ags_covid_rules

        Corona Regelungen nach AGS  # noqa: E501
        """
        pass

    def test_get_covid_infos(self):
        """Test case for get_covid_infos

        Allgemeine Informationen zu Corona  # noqa: E501
        """
        pass

    def test_get_covid_map(self):
        """Test case for get_covid_map

        Kartendaten für Corona-Fallzahlen.  # noqa: E501
        """
        pass

    def test_get_covid_ticker(self):
        """Test case for get_covid_ticker

        Covid-Ticker  # noqa: E501
        """
        pass

    def test_get_covid_ticker_message(self):
        """Test case for get_covid_ticker_message

        Detailinformationen zu Covid-Ticker Meldungen  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()