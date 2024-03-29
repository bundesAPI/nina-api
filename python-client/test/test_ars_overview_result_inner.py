"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.ars_overview_result_inner_i18n_title import (
    ARSOverviewResultInnerI18nTitle,
)
from deutschland.nina.model.ars_overview_result_inner_payload import (
    ARSOverviewResultInnerPayload,
)

from deutschland import nina

globals()["ARSOverviewResultInnerI18nTitle"] = ARSOverviewResultInnerI18nTitle
globals()["ARSOverviewResultInnerPayload"] = ARSOverviewResultInnerPayload
from deutschland.nina.model.ars_overview_result_inner import ARSOverviewResultInner


class TestARSOverviewResultInner(unittest.TestCase):
    """ARSOverviewResultInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testARSOverviewResultInner(self):
        """Test ARSOverviewResultInner"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ARSOverviewResultInner()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
