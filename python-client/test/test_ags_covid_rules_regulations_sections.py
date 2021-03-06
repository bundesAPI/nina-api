"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.ags_covid_rules_regulations_sections_bund import (
    AGSCovidRulesRegulationsSectionsBUND,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_kreis import (
    AGSCovidRulesRegulationsSectionsKREIS,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_land import (
    AGSCovidRulesRegulationsSectionsLAND,
)

from deutschland import nina

globals()["AGSCovidRulesRegulationsSectionsBUND"] = AGSCovidRulesRegulationsSectionsBUND
globals()[
    "AGSCovidRulesRegulationsSectionsKREIS"
] = AGSCovidRulesRegulationsSectionsKREIS
globals()["AGSCovidRulesRegulationsSectionsLAND"] = AGSCovidRulesRegulationsSectionsLAND
from deutschland.nina.model.ags_covid_rules_regulations_sections import (
    AGSCovidRulesRegulationsSections,
)


class TestAGSCovidRulesRegulationsSections(unittest.TestCase):
    """AGSCovidRulesRegulationsSections unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAGSCovidRulesRegulationsSections(self):
        """Test AGSCovidRulesRegulationsSections"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AGSCovidRulesRegulationsSections()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
