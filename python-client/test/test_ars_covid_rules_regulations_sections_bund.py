"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.ars_covid_rules_regulations_sections_bund_icon import (
    ARSCovidRulesRegulationsSectionsBUNDIcon,
)

from deutschland import nina

globals()[
    "ARSCovidRulesRegulationsSectionsBUNDIcon"
] = ARSCovidRulesRegulationsSectionsBUNDIcon
from deutschland.nina.model.ars_covid_rules_regulations_sections_bund import (
    ARSCovidRulesRegulationsSectionsBUND,
)


class TestARSCovidRulesRegulationsSectionsBUND(unittest.TestCase):
    """ARSCovidRulesRegulationsSectionsBUND unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testARSCovidRulesRegulationsSectionsBUND(self):
        """Test ARSCovidRulesRegulationsSectionsBUND"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ARSCovidRulesRegulationsSectionsBUND()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
