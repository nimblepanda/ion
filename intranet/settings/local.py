# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ipaddress
import logging
from .base import *


logger = logging.getLogger(__name__)

DEBUG = os.getenv("DEBUG", "TRUE") == "TRUE"

if os.getenv("WARN_INVALID_TEMPLATE_VARS", "NO") == "YES":
    class InvalidString(str):

        """An error for undefined context variables in templates."""

        def __mod__(self, other):
            logger.warning("Undefined variable or unknown value for: \"%s\"" % other)
            return ""

    TEMPLATES[0]["OPTIONS"]["string_if_invalid"] = InvalidString("%s")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ion",
        "USER": "ion",
        "PASSWORD": "pwd",
        "HOST": "localhost"
    }
}

SECRET_KEY = "crjl#r4(@8xv*x5ogeygrt@w%$$z9o8jlf7=25^!9k16pqsi!h"

CACHES["default"]["OPTIONS"]["DB"] = 2

if os.getenv("DUMMY_CACHE", "NO") == "YES":
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }

if os.getenv("SHORT_CACHE", "NO") == "YES":
    # Make the cache age last just long enough to reload the page to
    # check if caching worked
    for key in CACHE_AGE:
        CACHE_AGE[key] = 60

class ip_list(list):

    """A list of IP address strings."""

    def __contains__(self, key):
        """Check if a string matches an IP range in the list."""
        for item in self:
            if ipaddress.ip_address("{}".format(key)) in ipaddress.ip_network("{}".format(item)):
                return True
        return False

INTERNAL_IPS = ip_list([
    "127.0.0.0/8",
    "192.168.0.0/16",
    "198.38.16.0/20",
    "2001:468:cc0::/48"
])

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
