from django.conf.urls import patterns, include, url

from .views import list, add

urlpatterns = patterns('',
    url(r'^add/$', add),
    url(r'^$', list),
)
