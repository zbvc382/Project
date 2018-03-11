from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import home, requesters, authorisers, calendar

urlpatterns = [
    url(r'^$', home.home, name='home'),

    # Requester url patterns

    url(r'^requester/$', requesters.RequesterHomeView.as_view(), name='requester'),

    url(r'^requester/absence/(?:(?P<template>\d+)/)?$', requesters.RequesterRequestView.as_view(),
        name='absence'),

    url(r'^requester/absence/template=(?P<pk>\d+)/delete/$', requesters.RequesterDeleteTemplate.as_view(),
        name='delete'),

    url(r'^requester/absence/view/(?P<pk>\d+)/$', requesters.RequesterCheckView.as_view(), name='check'),

    url(r'^requester/absence/view/(?P<pk>\d+)/create-template/name=(?P<string>[\w.,\s]+)/$',
        requesters.RequesterCreateTemplate.as_view(), name='create'),

    url(r'^requester/absence/redo=(?P<pk>\d+)/$', requesters.RequesterRedoView.as_view(), name='redo'),

    # Authoriser url patterns

    url(r'^authoriser/$', authorisers.AuthoriserHomeView.as_view(), name='authoriser'),

    url(r'^authoriser/request/view/(?P<pk>\d+)/$', authorisers.AuthoriserRequestView.as_view(), name='request'),

    url(r'^authoriser/request/view/(?P<pk>\d+)/send/$', authorisers.AuthoriserRequestViewEmail.as_view(), name='send'),

    url(r'^authoriser/my_requesters/$', authorisers.AuthoriserMyRequestersView.as_view(), name='my_requesters'),

    url(r'^authoriser/my_requesters/user=(?P<pk>\d+)/create_restriction$',
        authorisers.AuthoriserCreateRestrictionView.as_view(), name='create_restriction'),

    url(r'^authoriser/my_requesters/restriction=(?P<pk>\d+)/remove_restriction$',
        authorisers.AuthoriserRemoveRestriction.as_view(), name='remove_restriction'),

    url(r'^admin/$', home.AdminRedirect.as_view(), name='admin'),

    url(r'^requester/latest/feed.ics$', calendar.EventFeed()),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)