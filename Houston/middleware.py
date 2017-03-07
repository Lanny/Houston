import time
import random

from Houston import utils
from Houston.models import *

HOUSTON_COOKIE_NAME = utils.get_setting('HOUSTON_COOKIE_NAME')

class TrackingSessionMiddleware(object):
    def process_response(self, request, response):
        if HOUSTON_COOKIE_NAME not in request.COOKIES:
            session = Session()
            session.save()
            response.set_cookie(HOUSTON_COOKIE_NAME,
                                session.id,
                                max_age=60*60*24*356)

        return response
