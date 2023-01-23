# nina.DefaultApi

All URIs are relative to *https://warnung.bund.de/api31*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_version**](DefaultApi.md#get_data_version) | **GET** /dynamic/version/dataVersion.json | Liefert die Versionsnummer.
[**get_event_code**](DefaultApi.md#get_event_code) | **GET** /appdata/gsb/eventCodes/{filename} | Event Code Bilddateien.
[**get_event_codes**](DefaultApi.md#get_event_codes) | **GET** /appdata/gsb/eventCodes/eventCodes.json | Liefert Event Codes und Name der Bilddateien.
[**get_faqs**](DefaultApi.md#get_faqs) | **GET** /appdata/gsb/faqs/DE/faq.json | FAQs
[**get_logo**](DefaultApi.md#get_logo) | **GET** /appdata/gsb/logos/{filename} | Logo-Bilddateien.
[**get_logos**](DefaultApi.md#get_logos) | **GET** /appdata/gsb/logos/logos.json | Liefert Namen und Logos für Sender-IDs
[**get_notfalltipps**](DefaultApi.md#get_notfalltipps) | **GET** /appdata/gsb/notfalltipps/DE/notfalltipps.json | Notfalltipps


# **get_data_version**
> VersionCollection get_data_version()

Liefert die Versionsnummer.

Liefert die Versionsnummer.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.version_collection import VersionCollection
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liefert die Versionsnummer.
        api_response = api_instance.get_data_version()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->get_data_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionCollection**](VersionCollection.md)

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

# **get_event_code**
> file_type get_event_code(filename)

Event Code Bilddateien.

Die verfügbaren Bilddateien und zugehörige Event Codes sind über /appdata/gsb/eventCodes/eventCodes.json abrufbar.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filename = "BBK-EVC-001.png" # str | Logo-Dateiname

    # example passing only required values which don't have defaults set
    try:
        # Event Code Bilddateien.
        api_response = api_instance.get_event_code(filename)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->get_event_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Logo-Dateiname |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_codes**
> EventCodeCollection get_event_codes()

Liefert Event Codes und Name der Bilddateien.

Liefert Event Codes und Name der Bilddateien für verschiedene Event Codes.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.event_code_collection import EventCodeCollection
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liefert Event Codes und Name der Bilddateien.
        api_response = api_instance.get_event_codes()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->get_event_codes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EventCodeCollection**](EventCodeCollection.md)

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

# **get_faqs**
> FAQCollection get_faqs()

FAQs

FAQs rund um die Warn-App NINA.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.faq_collection import FAQCollection
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # FAQs
        api_response = api_instance.get_faqs()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->get_faqs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FAQCollection**](FAQCollection.md)

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

# **get_logo**
> file_type get_logo(filename)

Logo-Bilddateien.

Die verfügbaren Bilddateien und zugehörige Sender-IDs + Namen sind über /appdata/gsb/logos/logos.json abrufbar.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filename = "dwd_logo.png" # str | Logo-Dateiname

    # example passing only required values which don't have defaults set
    try:
        # Logo-Bilddateien.
        api_response = api_instance.get_logo(filename)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->get_logo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Logo-Dateiname |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/jpeg


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logos**
> LogoCollection get_logos()

Liefert Namen und Logos für Sender-IDs

Liefert Namen und Logos für Sender-IDs

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.logo_collection import LogoCollection
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liefert Namen und Logos für Sender-IDs
        api_response = api_instance.get_logos()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->get_logos: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LogoCollection**](LogoCollection.md)

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

# **get_notfalltipps**
> Notfalltipps get_notfalltipps()

Notfalltipps

Liefert eine List von Notfalltipps für verschiedene Gefahrenlagen.

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.notfalltipps import Notfalltipps
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Notfalltipps
        api_response = api_instance.get_notfalltipps()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->get_notfalltipps: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Notfalltipps**](Notfalltipps.md)

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

