import random
from datetime import timedelta

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from Houston.models import *

url_patterns = (
    ('/', 0),
    ('pathing-test/%d', 1)
)

class Command(BaseCommand):
    help = ('Creates N new views evenly spread over the last K days, '
            'from J sessions.')

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)
        parser.add_argument('k', type=int)
        parser.add_argument('j', type=int)

    def handle(self, *args, **kwargs):
        sessions = []
        for _ in xrange(kwargs.get('k', 1)):
            session = Session()
            session.save()
            session.created = timezone.now() - timedelta(days=kwargs.get('j', 7))
            session.save()

            ip = '%d.%d.%d.%d' % tuple([random.randint(0,255) for _ in range(4)])

            sessions.append((session, ip))

        secs = timedelta(days=kwargs.get('j', 7)).total_seconds()
        for _ in xrange(kwargs.get('n', 0)):
            ctime = timezone.now() - timedelta(seconds=random.random()*secs)
            session, ip = random.choice(sessions)

            path_template, subs = random.choice(url_patterns)
            path = path_template % tuple([random.randint(0,255) for _ in range(subs)])

            view = PageView(
                path=path,
                report_time=ctime,
                session=session)

            view.save()
