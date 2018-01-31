from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.RequesterHomeView.as_view(), name='home'),
    url(r'^request/', login_required(views.RequestView.as_view()), name='request')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)