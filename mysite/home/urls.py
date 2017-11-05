from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^request/', views.form_request, name='request')
]