from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('Website.views',
    url(r'^$', 'index'),
    url(r'^index/$', 'index')
)
