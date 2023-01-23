# nina.CovidApi

All URIs are relative to *https://warnung.bund.de/api31*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ags_covid_rules**](CovidApi.md#get_ags_covid_rules) | **GET** /appdata/covid/covidrules/DE/{AGS}.json | Corona Regelungen nach AGS
[**get_covid_infos**](CovidApi.md#get_covid_infos) | **GET** /appdata/covid/covidinfos/DE/covidinfos.json | Allgemeine Informationen zu Corona
[**get_covid_map**](CovidApi.md#get_covid_map) | **GET** /appdata/covid/covidmap/DE/covidmap.json | Kartendaten für Corona-Fallzahlen.
[**get_covid_ticker**](CovidApi.md#get_covid_ticker) | **GET** /appdata/covid/covidticker/DE/covidticker.json | Covid-Ticker
[**get_covid_ticker_message**](CovidApi.md#get_covid_ticker_message) | **GET** /appdata/covid/covidticker/DE/tickermeldungen/{id}.json | Detailinformationen zu Covid-Ticker Meldungen
[**get_dashboard**](CovidApi.md#get_dashboard) | **GET** /dashboard/{AGS}.json | Meldungsübersicht nach AGS


# **get_ags_covid_rules**
> AGSCovidRules get_ags_covid_rules(ags)

Corona Regelungen nach AGS

Erhalten Sie die aktuellen Corona Regelungen für eine bestimmte Region.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import covid_api
from deutschland.nina.model.ags_covid_rules import AGSCovidRules
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_api.CovidApi(api_client)
    ags = "091620000000" # str | Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden.

    # example passing only required values which don't have defaults set
    try:
        # Corona Regelungen nach AGS
        api_response = api_instance.get_ags_covid_rules(ags)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling CovidApi->get_ags_covid_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ags** | **str**| Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. |

### Return type

[**AGSCovidRules**](AGSCovidRules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_covid_infos**
> CovidInfos get_covid_infos()

Allgemeine Informationen zu Corona

Erhalten Sie allgemeine Informationen zu Corona.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import covid_api
from deutschland.nina.model.covid_infos import CovidInfos
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_api.CovidApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Allgemeine Informationen zu Corona
        api_response = api_instance.get_covid_infos()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling CovidApi->get_covid_infos: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CovidInfos**](CovidInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_covid_map**
> CovidMap get_covid_map()

Kartendaten für Corona-Fallzahlen.

Die zugehörigen Geometrie-Daten sind über [https://warnung.bund.de/assets/json/converted_corona_kreise.json](https://warnung.bund.de/assets/json/converted_corona_kreise.json) abrufbar.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import covid_api
from deutschland.nina.model.covid_map import CovidMap
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_api.CovidApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Kartendaten für Corona-Fallzahlen.
        api_response = api_instance.get_covid_map()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling CovidApi->get_covid_map: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CovidMap**](CovidMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_covid_ticker**
> CovidTicker get_covid_ticker()

Covid-Ticker

Erhalten Sie die aktuellen Covid-Ticker Meldungen.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import covid_api
from deutschland.nina.model.covid_ticker import CovidTicker
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_api.CovidApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Covid-Ticker
        api_response = api_instance.get_covid_ticker()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling CovidApi->get_covid_ticker: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CovidTicker**](CovidTicker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_covid_ticker_message**
> CovidTickerMessage get_covid_ticker_message(id)

Detailinformationen zu Covid-Ticker Meldungen

Erhalten Sie Detailinformationen zu Covid-Ticker Meldungen.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import covid_api
from deutschland.nina.model.covid_ticker_message import CovidTickerMessage
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_api.CovidApi(api_client)
    id = "7eb928fc-4496-4a71-8154-1c64be10ce0a" # str | Covid-Ticker meldung. Aktuelle Meldungen können über /appdata/covid/covidticker/DE/covidticker.json abgerufen werden.

    # example passing only required values which don't have defaults set
    try:
        # Detailinformationen zu Covid-Ticker Meldungen
        api_response = api_instance.get_covid_ticker_message(id)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling CovidApi->get_covid_ticker_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Covid-Ticker meldung. Aktuelle Meldungen können über /appdata/covid/covidticker/DE/covidticker.json abgerufen werden. |

### Return type

[**CovidTickerMessage**](CovidTickerMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> AGSOverviewResult get_dashboard(ags)

Meldungsübersicht nach AGS

Erhalten Sie die aktuellen Warnmeldungen für eine bestimmte Region.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import covid_api
from deutschland.nina.model.ags_overview_result import AGSOverviewResult
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_api.CovidApi(api_client)
    ags = "091620000000" # str | Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \"0000000\" ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel) bereitgestellt werden.

    # example passing only required values which don't have defaults set
    try:
        # Meldungsübersicht nach AGS
        api_response = api_instance.get_dashboard(ags)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling CovidApi->get_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ags** | **str**| Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \&quot;0000000\&quot; ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel) bereitgestellt werden. |

### Return type

[**AGSOverviewResult**](AGSOverviewResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

