# nina.WarningsApi

All URIs are relative to *https://warnung.bund.de/api31*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_biwapp_map_data**](WarningsApi.md#get_biwapp_map_data) | **GET** /biwapp/mapData.json | Biwapp Meldungen
[**get_dwd_map_data**](WarningsApi.md#get_dwd_map_data) | **GET** /dwd/mapData.json | Unwetterwarnungen des Deutschen Wetterdienstes
[**get_katwarn_map_data**](WarningsApi.md#get_katwarn_map_data) | **GET** /katwarn/mapData.json | Katwarn Meldungen
[**get_lhp_map_data**](WarningsApi.md#get_lhp_map_data) | **GET** /lhp/mapData.json | Meldungen des Länderübergreifenden Hochwasserportals
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

