from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import home, requester, authoriser

urlpatterns = [
    url(r'^$', home.home, name='home'),

    # Requester url patterns

    url(r'^requester/$', requester.RequesterHome.as_view(), name='requester'),

    url(r'^requester/request/new/(?:(?P<template>\d+)/)?$', requester.RequesterNewRequest.as_view(), name='new'),

    url(r'^requester/template=(?P<string>[\w.,;:!?@£$%&*^()_±/~`<>\s]+)/create/(?P<pk>\d+)/$',
        requester.RequesterCreateTemplate.as_view(), name='create'),

    url(r'^requester/template=(?P<pk>\d+)/delete/$', requester.RequesterDeleteTemplate.as_view(), name='delete'),

    url(r'^requester/request=(?P<pk>\d+)/view/$', requester.RequesterViewRequest.as_view(), name='requester_view'),

    url(r'^requester/request=(?P<pk>\d+)/reuse$', requester.RequesterReuseRequest.as_view(), name='reuse'),

    url(r'^requester/calendar/feed.ics$', requester.RequesterCalendarFeed(), name='feed'),

    # Authoriser url patterns

    url(r'^authoriser/$', authoriser.AuthoriserHome.as_view(), name='authoriser'),

    url(r'^authoriser/request=(?P<pk>\d+)/view/$', authoriser.AuthoriserViewRequest.as_view(), name='authoriser_view'),

    url(r'^authoriser/request=(?P<pk>\d+)/send/$', authoriser.AuthoriserSendEmail.as_view(), name='send'),

    url(r'^authoriser/requesters/$', authoriser.AuthoriserViewRequesters.as_view(), name='requesters'),

    url(r'^authoriser/user=(?P<pk>\d+)/restriction/$',
        authoriser.AuthoriserCreateRestriction.as_view(), name='restriction'),

    url(r'^authoriser/restriction=(?P<pk>\d+)/remove/$',
        authoriser.AuthoriserDeleteRestriction.as_view(), name='remove'),

    url(r'^admin/$', home.AdminRedirect.as_view(), name='admin'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
