from django.conf.urls import url
from GSTForm import views

urlpatterns = [
    url(r'^gst/$', views.GSTApi),
    url(r'^gst/([0-9])$', views.GSTApi),
]