import pytz
import datetime

from django.conf import settings

default_settings = {
    'HOUSTON_COOKIE_NAME': '_houston',
}

EPOCH = datetime.datetime(1970,1,1,0,0, tzinfo=pytz.utc)

def get_setting(setting_name):
    return getattr(settings, setting_name, default_settings[setting_name])

def to_unix_time(aware_datetime):
    assert aware_datetime.tzinfo

    return int((aware_datetime - EPOCH).total_seconds())

_blanks = {
    'month': ('day', 'hour', 'minute', 'second', 'microsecond'),
    'day': ('hour', 'minute', 'second', 'microsecond'),
    'hour': ('minute', 'second', 'microsecond'),
    'minute': ('second', 'microsecond'),
}

def truncate(dt, granularity):
    return dt.replace(**dict([(field, 0) for field in _blanks[granularity]]))

