from django.conf import settings
from django.db import models
from django.utils import timezone

HTTP_METHODS = ((x, x) for x in [
        'GET',
        'POST',
        'HEAD',
        'PUT',
        'DELETE',
        'CONNECT',
        'OPTIONS',
        'TRACE',
        'PATCH'
    ])


class PageView(models.Model):
    path = models.CharField(max_length=1024)
    query = models.CharField(max_length=1024)
    method = models.CharField(max_length=8, choices=HTTP_METHODS)
    report_time = models.DateTimeField(default=timezone.now)

    tt_load = models.IntegerField(null=True)
    req_time = models.IntegerField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
