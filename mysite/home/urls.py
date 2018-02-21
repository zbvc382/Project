from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import home, requesters, authorisers

urlpatterns = [
    url(r'^$', home.home, name='home'),
    url(r'^requester/', requesters.RequesterHomeView.as_view(), name='requester'),
    url(r'^authoriser/', authorisers.AuthoriserHomeView.as_view(), name='authoriser'),
    url(r'^absence/', requesters.RequesterRequestView.as_view(), name='absence'),
    url(r'^admin/', home.AdminRedirect.as_view(), name='admin'),
    url(r'^request/(?P<pk>\d+)/', authorisers.AuthoriserRequestView.as_view(), name='request'),
    url(r'^check/(?P<pk>\d+)/', requesters.RequesterCheckView.as_view(), name='check')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)