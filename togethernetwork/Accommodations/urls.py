# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('', 
    #url(r'^(?P<activity_pk>\d+)/book$', views.book_accommodation, name='book_accommodation'),
    #url(r'^(?P<activity_pk>\d+)$', views.single_accommodation, name='single_accommodation'),

    url(r'^list', views.accommodations_view, name='accommodations_view'), 
    url(r'^$', views.accommodations_view, name='accommodations_view'), 
)



