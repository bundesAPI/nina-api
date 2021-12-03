# nina
Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/bundesAPI/nina-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/bundesAPI/nina-api.git`)

Then import the package:
```python
from deutschland import nina
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
from deutschland import nina
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
from deutschland import nina
from pprint import pprint
from deutschland.nina.api import default_api
from deutschland.nina.model.ags_covid_rules import AGSCovidRules
from deutschland.nina.model.ags_overview_result import AGSOverviewResult
from deutschland.nina.model.map_warnings import MapWarnings
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)



# Enter a context with an instance of the API client
with nina.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    ags = "091620000000" # str | Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden.

    try:
        # Corona Regelungen nach AGS
        api_response = api_instance.appdata_covid_covidrules_deags_json_get(ags)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->appdata_covid_covidrules_deags_json_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://warnung.bund.de/api31*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**appdata_covid_covidrules_deags_json_get**](docs/DefaultApi.md#appdata_covid_covidrules_deags_json_get) | **GET** /appdata/covid/covidrules/DE/{AGS}.json | Corona Regelungen nach AGS
*DefaultApi* | [**biwapp_map_data_json_get**](docs/DefaultApi.md#biwapp_map_data_json_get) | **GET** /biwapp/mapData.json | Biwapp Meldungen
*DefaultApi* | [**dashboard_ags_json_get**](docs/DefaultApi.md#dashboard_ags_json_get) | **GET** /dashboard/{AGS}.json | Meldungsübersicht nach AGS
*DefaultApi* | [**katwarn_map_data_json_get**](docs/DefaultApi.md#katwarn_map_data_json_get) | **GET** /katwarn/mapData.json | Katwarn Meldungen
*DefaultApi* | [**mowas_map_data_json_get**](docs/DefaultApi.md#mowas_map_data_json_get) | **GET** /mowas/mapData.json | Mowas Meldungen


## Documentation For Models

 - [AGSCovidRules](docs/AGSCovidRules.md)
 - [AGSCovidRulesCommon](docs/AGSCovidRulesCommon.md)
 - [AGSCovidRulesIcon](docs/AGSCovidRulesIcon.md)
 - [AGSCovidRulesLevel](docs/AGSCovidRulesLevel.md)
 - [AGSCovidRulesRegulations](docs/AGSCovidRulesRegulations.md)
 - [AGSCovidRulesRegulationsSections](docs/AGSCovidRulesRegulationsSections.md)
 - [AGSCovidRulesRegulationsSectionsBUND](docs/AGSCovidRulesRegulationsSectionsBUND.md)
 - [AGSCovidRulesRegulationsSectionsBUNDIcon](docs/AGSCovidRulesRegulationsSectionsBUNDIcon.md)
 - [AGSCovidRulesRegulationsSectionsKREIS](docs/AGSCovidRulesRegulationsSectionsKREIS.md)
 - [AGSCovidRulesRegulationsSectionsKREISIcon](docs/AGSCovidRulesRegulationsSectionsKREISIcon.md)
 - [AGSCovidRulesRegulationsSectionsLAND](docs/AGSCovidRulesRegulationsSectionsLAND.md)
 - [AGSCovidRulesRegulationsSectionsLANDIcon](docs/AGSCovidRulesRegulationsSectionsLANDIcon.md)
 - [AGSCovidRulesRules](docs/AGSCovidRulesRules.md)
 - [AGSOverviewResult](docs/AGSOverviewResult.md)
 - [MapWarnings](docs/MapWarnings.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

kontakt@bund.dev


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in nina.apis and nina.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from deutschland.nina.api.default_api import DefaultApi`
- `from deutschland.nina.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
from deutschland import nina
from deutschland.nina.apis import *
from deutschland.nina.models import *
```
