"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.ags_overview_result_inner_i18n_title import (
    AGSOverviewResultInnerI18nTitle,
)
from deutschland.nina.model.ags_overview_result_inner_payload import (
    AGSOverviewResultInnerPayload,
)

from deutschland import nina

globals()["AGSOverviewResultInnerI18nTitle"] = AGSOverviewResultInnerI18nTitle
globals()["AGSOverviewResultInnerPayload"] = AGSOverviewResultInnerPayload
from deutschland.nina.model.ags_overview_result_inner import AGSOverviewResultInner


class TestAGSOverviewResultInner(unittest.TestCase):
    """AGSOverviewResultInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAGSOverviewResultInner(self):
        """Test AGSOverviewResultInner"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AGSOverviewResultInner()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()