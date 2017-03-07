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

