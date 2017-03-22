import json

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.aggregates import Count
from django.db.models.functions import Trunc
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from Houston import forms
from Houston.models import *

def record_page_view(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request method',
                                      content_type='text/plain')

    form = forms.PageViewForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest('Invalid params',
                                      content_type='text/plain')
    else:
        view = PageView(
            path=form.cleaned_data['path'],
            session=Session.get_session(request))

        if request.user.is_authenticated():
            view.user = request.user

        view.save()

        return HttpResponse('success', content_type='text/plain')

@staff_member_required
def view_counts(request):
    form = forms.ViewCountsForm(request.GET)

    if not form.is_valid():
        response_data = {
            'status': 'FAILURE',
            'errors': form.errors
        }

        return HttpResponseBadRequest(json.dumps(response_data),
                                      content_type='application/json')

    start_time = form.cleaned_data['start_time']
    end_time = form.cleaned_data['end_time']
    granularity = form.cleaned_data['granularity']

    view_counts = list(PageView.objects.all()
        .filter(report_time__gte=start_time,
                report_time__lte=end_time)
        .annotate(bucket=Trunc('report_time', kind=granularity))
        .values('bucket')
        .annotate(count=Count('bucket'))
        .order_by('-bucket'))

    values = []
    for bucket in view_counts:
        values.append({
            'count': bucket['count'],
            'bucket': utils.to_unix_time(bucket['bucket'])
        })

    return HttpResponse(json.dumps({
        'status': 'SUCCESS',
        'firstBucket': utils.to_unix_time(utils.truncate(start_time, granularity)),
        'lastBucket': utils.to_unix_time(utils.truncate(end_time, granularity)),
        'viewCounts': values
    }), content_type='application/json')
