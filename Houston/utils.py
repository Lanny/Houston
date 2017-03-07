from django.conf import settings

default_settings = {
    'HOUSTON_COOKIE_NAME': '_houston',
}

def get_setting(setting_name):
    return getattr(settings, setting_name, default_settings[setting_name])
