"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.ags_covid_rules_regulations_sections import (
    AGSCovidRulesRegulationsSections,
)

from deutschland import nina

globals()["AGSCovidRulesRegulationsSections"] = AGSCovidRulesRegulationsSections
from deutschland.nina.model.ags_covid_rules_regulations import AGSCovidRulesRegulations


class TestAGSCovidRulesRegulations(unittest.TestCase):
    """AGSCovidRulesRegulations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAGSCovidRulesRegulations(self):
        """Test AGSCovidRulesRegulations"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AGSCovidRulesRegulations()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
