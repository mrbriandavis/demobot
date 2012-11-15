from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#from django.conf.urls.defaults import *
from hackday.api import EventResource

event_resource = EventResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'orchestrator.views.home', name='home'),
    # url(r'^orchestrator/', include('orchestrator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^hackday/$', 'hackday.views.index'),
    url(r'^hackday/(?P<poll_id>\d+)/$', 'hackday.views.detail'),
    url(r'^hackday/(?P<poll_id>\d+)/results/$', 'hackday.views.results'),
    url(r'^hackday/(?P<poll_id>\d+)/vote/$', 'hackday.views.vote'),
#    url(r'^api/event/$', 'hackday.views.event'),
    (r'^api/', include(event_resource.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
