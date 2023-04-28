# nina.WarningsApi

All URIs are relative to *https://warnung.bund.de/api31*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_biwapp_map_data**](WarningsApi.md#get_biwapp_map_data) | **GET** /biwapp/mapData.json | Biwapp Meldungen
[**get_dashboard**](WarningsApi.md#get_dashboard) | **GET** /dashboard/{ARS}.json | Meldungsübersicht nach ARS
[**get_dwd_map_data**](WarningsApi.md#get_dwd_map_data) | **GET** /dwd/mapData.json | Unwetterwarnungen des Deutschen Wetterdienstes
[**get_katwarn_map_data**](WarningsApi.md#get_katwarn_map_data) | **GET** /katwarn/mapData.json | Katwarn Meldungen
[**get_lhp_map_data**](WarningsApi.md#get_lhp_map_data) | **GET** /lhp/mapData.json | Meldungen des Länderübergreifenden Hochwasserportals
[**get_mo_wa_srss_feed**](WarningsApi.md#get_mo_wa_srss_feed) | **GET** /mowas/rss/{ARS}.rss | MoWaS Meldungen als RSS-Feed
[**get_mowas_map_data**](WarningsApi.md#get_mowas_map_data) | **GET** /mowas/mapData.json | Mowas Meldungen
[**get_police_map_data**](WarningsApi.md#get_police_map_data) | **GET** /police/mapData.json | Polizeimeldungen
[**get_warning**](WarningsApi.md#get_warning) | **GET** /warnings/{identifier}.json | Detailinformation zu einer Warnung
[**get_warning_geo_json**](WarningsApi.md#get_warning_geo_json) | **GET** /warnings/{identifier}.geojson | GeoJSON informationen zu einer Warnung.


# **get_biwapp_map_data**
> MapWarnings get_biwapp_map_data()

Biwapp Meldungen

Liefert die Biwapp-Meldungen für die Kartenansicht.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Biwapp Meldungen
        api_response = api_instance.get_biwapp_map_data()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_biwapp_map_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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
> ARSOverviewResult get_dashboard(ars)

Meldungsübersicht nach ARS

Erhalten Sie die aktuellen Warnmeldungen für eine bestimmte Region.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.ars_overview_result import ARSOverviewResult
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)
    ars = "091620000000" # str | Amtlicher Regionalschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \"0000000\" ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel#Regionalschl%C3%BCssel) bereitgestellt werden.

    # example passing only required values which don't have defaults set
    try:
        # Meldungsübersicht nach ARS
        api_response = api_instance.get_dashboard(ars)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ars** | **str**| Amtlicher Regionalschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \&quot;0000000\&quot; ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel#Regionalschl%C3%BCssel) bereitgestellt werden. |

### Return type

[**ARSOverviewResult**](ARSOverviewResult.md)

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

# **get_dwd_map_data**
> MapWarnings get_dwd_map_data()

Unwetterwarnungen des Deutschen Wetterdienstes

Liefert die Unwetterwarnungen des Deutschen Wetterdienstes für die Kartenansicht.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Unwetterwarnungen des Deutschen Wetterdienstes
        api_response = api_instance.get_dwd_map_data()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_dwd_map_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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

# **get_katwarn_map_data**
> MapWarnings get_katwarn_map_data()

Katwarn Meldungen

Liefert die Katwarn-Meldungen für die Kartenansicht.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Katwarn Meldungen
        api_response = api_instance.get_katwarn_map_data()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_katwarn_map_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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

# **get_lhp_map_data**
> MapWarnings get_lhp_map_data()

Meldungen des Länderübergreifenden Hochwasserportals

Liefert die Meldungen des Länderübergreifenden Hochwasserportals für die Kartenansicht.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Meldungen des Länderübergreifenden Hochwasserportals
        api_response = api_instance.get_lhp_map_data()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_lhp_map_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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

# **get_mo_wa_srss_feed**
> Rss get_mo_wa_srss_feed(ars)

MoWaS Meldungen als RSS-Feed

Erhalte alle aktuellen MoWaS Meldungen einer Region als RSS-Feed.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.rss import Rss
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)
    ars = "091620000000" # str | Amtlicher Regionalschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \"0000000\" ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel#Regionalschl%C3%BCssel) bereitgestellt werden.

    # example passing only required values which don't have defaults set
    try:
        # MoWaS Meldungen als RSS-Feed
        api_response = api_instance.get_mo_wa_srss_feed(ars)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_mo_wa_srss_feed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ars** | **str**| Amtlicher Regionalschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \&quot;0000000\&quot; ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel#Regionalschl%C3%BCssel) bereitgestellt werden. |

### Return type

[**Rss**](Rss.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/rss+xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mowas_map_data**
> MapWarnings get_mowas_map_data()

Mowas Meldungen

Liefert die Mowas-Meldungen für die Kartenansicht.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Mowas Meldungen
        api_response = api_instance.get_mowas_map_data()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_mowas_map_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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

# **get_police_map_data**
> MapWarnings get_police_map_data()

Polizeimeldungen

Liefert die Polizeimeldungen für die Kartenansicht.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Polizeimeldungen
        api_response = api_instance.get_police_map_data()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_police_map_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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

# **get_warning**
> Warning get_warning(identifier)

Detailinformation zu einer Warnung

Detailinformation zu einer Warnung

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from deutschland.nina.model.warning import Warning
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)
    identifier = "kat.1234567890abcdef12345678_public_topics" # str | Meldungs-ID

    # example passing only required values which don't have defaults set
    try:
        # Detailinformation zu einer Warnung
        api_response = api_instance.get_warning(identifier)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_warning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Meldungs-ID |

### Return type

[**Warning**](Warning.md)

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

# **get_warning_geo_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_warning_geo_json(identifier)

GeoJSON informationen zu einer Warnung.

Datenformat entspricht [https://datatracker.ietf.org/doc/html/rfc7946#section-3](https://datatracker.ietf.org/doc/html/rfc7946#section-3)

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import warnings_api
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = warnings_api.WarningsApi(api_client)
    identifier = "kat.1234567890abcdef12345678_public_topics" # str | Meldungs-ID

    # example passing only required values which don't have defaults set
    try:
        # GeoJSON informationen zu einer Warnung.
        api_response = api_instance.get_warning_geo_json(identifier)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling WarningsApi->get_warning_geo_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Meldungs-ID |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

