# nina.ArchiveApi

All URIs are relative to *https://warnung.bund.de/api31*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_full_warning_history**](ArchiveApi.md#get_full_warning_history) | **GET** /archive.mowas/{identifier}-mapping.json | Gesammelter Verlauf einer MOWAS Warnung
[**get_warning_history**](ArchiveApi.md#get_warning_history) | **GET** /archive.mowas/{identifier}.json | Abruf einer archivierten MOWAS Warnung


# **get_full_warning_history**
> ArchiveWarningHistory get_full_warning_history(identifier)

Gesammelter Verlauf einer MOWAS Warnung

Gesammelter Verlauf einer MOWAS Warnung

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import archive_api
from deutschland.nina.model.archive_warning_history import ArchiveWarningHistory
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = archive_api.ArchiveApi(api_client)
    identifier = "mow.DE-NI-OL-W015-20230121-002" # str | Meldungs-ID

    # example passing only required values which don't have defaults set
    try:
        # Gesammelter Verlauf einer MOWAS Warnung
        api_response = api_instance.get_full_warning_history(identifier)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling ArchiveApi->get_full_warning_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Meldungs-ID |

### Return type

[**ArchiveWarningHistory**](ArchiveWarningHistory.md)

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

# **get_warning_history**
> Warning get_warning_history(identifier)

Abruf einer archivierten MOWAS Warnung

Abruf einer archivierten MOWAS Warnung

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import archive_api
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
    api_instance = archive_api.ArchiveApi(api_client)
    identifier = "mow.DE-NI-OL-W015-20230121-001_20230121112659" # str | Meldungs-ID, gefolgt von \"_\" mit angehangenem Zeitstempel der Warnung im Format YYYYMMDDHHMMSS

    # example passing only required values which don't have defaults set
    try:
        # Abruf einer archivierten MOWAS Warnung
        api_response = api_instance.get_warning_history(identifier)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling ArchiveApi->get_warning_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Meldungs-ID, gefolgt von \&quot;_\&quot; mit angehangenem Zeitstempel der Warnung im Format YYYYMMDDHHMMSS |

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

