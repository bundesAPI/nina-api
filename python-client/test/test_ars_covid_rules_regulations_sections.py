"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.ars_covid_rules_regulations_sections_bund import (
    ARSCovidRulesRegulationsSectionsBUND,
)
from deutschland.nina.model.ars_covid_rules_regulations_sections_kreis import (
    ARSCovidRulesRegulationsSectionsKREIS,
)
from deutschland.nina.model.ars_covid_rules_regulations_sections_land import (
    ARSCovidRulesRegulationsSectionsLAND,
)

from deutschland import nina

globals()["ARSCovidRulesRegulationsSectionsBUND"] = ARSCovidRulesRegulationsSectionsBUND
globals()[
    "ARSCovidRulesRegulationsSectionsKREIS"
] = ARSCovidRulesRegulationsSectionsKREIS
globals()["ARSCovidRulesRegulationsSectionsLAND"] = ARSCovidRulesRegulationsSectionsLAND
from deutschland.nina.model.ars_covid_rules_regulations_sections import (
    ARSCovidRulesRegulationsSections,
)


class TestARSCovidRulesRegulationsSections(unittest.TestCase):
    """ARSCovidRulesRegulationsSections unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testARSCovidRulesRegulationsSections(self):
        """Test ARSCovidRulesRegulationsSections"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ARSCovidRulesRegulationsSections()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
