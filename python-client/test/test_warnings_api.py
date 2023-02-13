"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.nina.api.warnings_api import WarningsApi  # noqa: E501

from deutschland import nina


class TestWarningsApi(unittest.TestCase):
    """WarningsApi unit test stubs"""

    def setUp(self):
        self.api = WarningsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_biwapp_map_data(self):
        """Test case for get_biwapp_map_data

        Biwapp Meldungen  # noqa: E501
        """
        pass

    def test_get_dashboard(self):
        """Test case for get_dashboard

        Meldungsübersicht nach AGS  # noqa: E501
        """
        pass

    def test_get_dwd_map_data(self):
        """Test case for get_dwd_map_data

        Unwetterwarnungen des Deutschen Wetterdienstes  # noqa: E501
        """
        pass

    def test_get_katwarn_map_data(self):
        """Test case for get_katwarn_map_data

        Katwarn Meldungen  # noqa: E501
        """
        pass

    def test_get_lhp_map_data(self):
        """Test case for get_lhp_map_data

        Meldungen des Länderübergreifenden Hochwasserportals  # noqa: E501
        """
        pass

    def test_get_mowas_map_data(self):
        """Test case for get_mowas_map_data

        Mowas Meldungen  # noqa: E501
        """
        pass

    def test_get_police_map_data(self):
        """Test case for get_police_map_data

        Polizeimeldungen  # noqa: E501
        """
        pass

    def test_get_warning(self):
        """Test case for get_warning

        Detailinformation zu einer Warnung  # noqa: E501
        """
        pass

    def test_get_warning_geo_json(self):
        """Test case for get_warning_geo_json

        GeoJSON informationen zu einer Warnung.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
