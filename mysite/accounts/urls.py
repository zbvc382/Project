from django.conf.urls import url
from . import views

from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html', 'redirect_authenticated_user': True}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'})
]