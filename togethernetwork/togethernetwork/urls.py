# -*- coding=utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'togethernetwork.views.home', name='home'),
    # url(r'^togethernetwork/', include('togethernetwork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^activities/', include('Activities.urls')),
    url(r'', include('Mainpages.urls')),
)