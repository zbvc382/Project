from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import requesters, home

urlpatterns = [
    url(r'^$', home.home, name='home'),
    url(r'^requester/', requesters.RequesterHomeView.as_view(), name='requester'),
    url(r'^absence/', requesters.RequestView.as_view(), name='absence'),
    url(r'^admin/', home.AdminRedirect.as_view(), name='admin'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)