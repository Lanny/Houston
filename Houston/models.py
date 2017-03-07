import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from Houston import utils

HOUSTON_COOKIE_NAME = utils.get_setting('HOUSTON_COOKIE_NAME')

class PageView(models.Model):
    path = models.CharField(max_length=1024)
    query = models.CharField(max_length=1024, default='')
    report_time = models.DateTimeField(default=timezone.now)

    tt_load = models.IntegerField(null=True)
    req_time = models.IntegerField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    session = models.ForeignKey('Houston.Session', null=True)

class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_session(cls, request):
        session_id = request.COOKIES.get(HOUSTON_COOKIE_NAME, None)

        if not session_id:
            return None

        try:
            session = cls.objects.get(pk=session_id)
            return session

        except cls.DoesNotExist:
            return None

    def __unicode__(self):
        return str(self.id)
