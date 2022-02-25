from django.conf.urls import url
from start import views

urlpatterns = [
    url(r'^api/start/$', views.startApi),
    url(r'^api/start/([0-9])$', views.startApi),
]