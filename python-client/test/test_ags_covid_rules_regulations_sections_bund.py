"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.ags_covid_rules_regulations_sections_bund_icon import (
    AGSCovidRulesRegulationsSectionsBUNDIcon,
)

from deutschland import nina

globals()[
    "AGSCovidRulesRegulationsSectionsBUNDIcon"
] = AGSCovidRulesRegulationsSectionsBUNDIcon
from deutschland.nina.model.ags_covid_rules_regulations_sections_bund import (
    AGSCovidRulesRegulationsSectionsBUND,
)


class TestAGSCovidRulesRegulationsSectionsBUND(unittest.TestCase):
    """AGSCovidRulesRegulationsSectionsBUND unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAGSCovidRulesRegulationsSectionsBUND(self):
        """Test AGSCovidRulesRegulationsSectionsBUND"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AGSCovidRulesRegulationsSectionsBUND()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
