"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.covid_infos_article import CovidInfosArticle
from deutschland.nina.model.covid_infos_image import CovidInfosImage

from deutschland import nina

globals()["CovidInfosArticle"] = CovidInfosArticle
globals()["CovidInfosImage"] = CovidInfosImage
from deutschland.nina.model.covid_infos_tip import CovidInfosTip


class TestCovidInfosTip(unittest.TestCase):
    """CovidInfosTip unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCovidInfosTip(self):
        """Test CovidInfosTip"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CovidInfosTip()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
