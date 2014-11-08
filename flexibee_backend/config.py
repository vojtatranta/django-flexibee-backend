import sys

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


FLEXIBEE_COMPANY_MODEL = getattr(settings, 'FLEXIBEE_COMPANY_MODEL', None)
FLEXIBEE_BACKEND_NAME = getattr(settings, 'FLEXIBEE_BACKEND_NAME', 'flexibee')
TESTING = sys.argv[1:2] == ['test'] or sys.argv[1:2] == ['jenkins']
FLEXIBEE_EXTERNAL_KEY_PREFIX = getattr(settings, 'FLEXIBEE_EXTERNAL_KEY_PREFIX', None)

if not FLEXIBEE_EXTERNAL_KEY_PREFIX:
    raise ImproperlyConfigured('FLEXIBEE_EXTERNAL_KEY_PREFIX must be set inside settings')
