from django.views.generic import TemplateView

from django.conf.urls import include, url
from django.contrib import admin

from testsite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^houston/', include('Houston.urls')),
    url(r'^$', TemplateView.as_view(template_name='testsite/index.html')),
    url(r'^pathing-test/(?P<pk_sorta_lol>\d+)/?$', views.pathed_view, 
        name='pathed-view')
]
