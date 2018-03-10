from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html', 'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout')
]
