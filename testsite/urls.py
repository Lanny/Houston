from django.views.generic import TemplateView

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^houston/', include('Houston.urls')),
    url(r'^$', TemplateView.as_view(template_name='testsite/index.html'))
]
