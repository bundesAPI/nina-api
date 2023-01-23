# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.nina.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.nina.model.ags_covid_rules import AGSCovidRules
from deutschland.nina.model.ags_covid_rules_common_inner import AGSCovidRulesCommonInner
from deutschland.nina.model.ags_covid_rules_level import AGSCovidRulesLevel
from deutschland.nina.model.ags_covid_rules_regulations import AGSCovidRulesRegulations
from deutschland.nina.model.ags_covid_rules_regulations_sections import (
    AGSCovidRulesRegulationsSections,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_bund import (
    AGSCovidRulesRegulationsSectionsBUND,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_bund_icon import (
    AGSCovidRulesRegulationsSectionsBUNDIcon,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_kreis import (
    AGSCovidRulesRegulationsSectionsKREIS,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_kreis_icon import (
    AGSCovidRulesRegulationsSectionsKREISIcon,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_land import (
    AGSCovidRulesRegulationsSectionsLAND,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_land_icon import (
    AGSCovidRulesRegulationsSectionsLANDIcon,
)
from deutschland.nina.model.ags_covid_rules_rules_inner import AGSCovidRulesRulesInner
from deutschland.nina.model.ags_covid_rules_rules_inner_icon import (
    AGSCovidRulesRulesInnerIcon,
)
from deutschland.nina.model.ags_overview_result import AGSOverviewResult
from deutschland.nina.model.ags_overview_result_inner import AGSOverviewResultInner
from deutschland.nina.model.ags_overview_result_inner_i18n_title import (
    AGSOverviewResultInnerI18nTitle,
)
from deutschland.nina.model.ags_overview_result_inner_payload import (
    AGSOverviewResultInnerPayload,
)
from deutschland.nina.model.ags_overview_result_inner_payload_data import (
    AGSOverviewResultInnerPayloadData,
)
from deutschland.nina.model.ags_overview_result_inner_payload_data_area import (
    AGSOverviewResultInnerPayloadDataArea,
)
from deutschland.nina.model.ags_overview_result_inner_payload_data_trans_keys import (
    AGSOverviewResultInnerPayloadDataTransKeys,
)
from deutschland.nina.model.covid_infos import CovidInfos
from deutschland.nina.model.covid_infos_article import CovidInfosArticle
from deutschland.nina.model.covid_infos_category import CovidInfosCategory
from deutschland.nina.model.covid_infos_image import CovidInfosImage
from deutschland.nina.model.covid_infos_tip import CovidInfosTip
from deutschland.nina.model.covid_map import CovidMap
from deutschland.nina.model.covid_map_data import CovidMapData
from deutschland.nina.model.covid_map_legend import CovidMapLegend
from deutschland.nina.model.covid_map_style import CovidMapStyle
from deutschland.nina.model.covid_ticker import CovidTicker
from deutschland.nina.model.covid_ticker_entry import CovidTickerEntry
from deutschland.nina.model.covid_ticker_message import CovidTickerMessage
from deutschland.nina.model.event_code import EventCode
from deutschland.nina.model.event_code_collection import EventCodeCollection
from deutschland.nina.model.faq import FAQ
from deutschland.nina.model.faq_collection import FAQCollection
from deutschland.nina.model.key_value_array import KeyValueArray
from deutschland.nina.model.key_value_array_inner import KeyValueArrayInner
from deutschland.nina.model.logo import Logo
from deutschland.nina.model.logo_collection import LogoCollection
from deutschland.nina.model.map_warnings import MapWarnings
from deutschland.nina.model.map_warnings_inner import MapWarningsInner
from deutschland.nina.model.map_warnings_inner_i18n_title import (
    MapWarningsInnerI18nTitle,
)
from deutschland.nina.model.notfalltipps import Notfalltipps
from deutschland.nina.model.notfalltipps_article import NotfalltippsArticle
from deutschland.nina.model.notfalltipps_category import NotfalltippsCategory
from deutschland.nina.model.notfalltipps_collection import NotfalltippsCollection
from deutschland.nina.model.notfalltipps_image import NotfalltippsImage
from deutschland.nina.model.notfalltipps_tip import NotfalltippsTip
from deutschland.nina.model.version import Version
from deutschland.nina.model.version_collection import VersionCollection
from deutschland.nina.model.warning import Warning
from deutschland.nina.model.warning_info_inner import WarningInfoInner
from deutschland.nina.model.warning_info_inner_area_inner import (
    WarningInfoInnerAreaInner,
)
