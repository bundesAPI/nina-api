# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from deutschland.nina.api.archive_api import ArchiveApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.nina.api.archive_api import ArchiveApi
from deutschland.nina.api.covid_api import CovidApi
from deutschland.nina.api.default_api import DefaultApi
from deutschland.nina.api.warnings_api import WarningsApi
