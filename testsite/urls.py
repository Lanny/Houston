from django.views.generic import TemplateView

from django.conf.urls import url
from django.contrib import admin

import Houston

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^houston/', Houston.site.urls),
    url(r'^$', TemplateView.as_view(template_name='testsite/index.html'))
]
