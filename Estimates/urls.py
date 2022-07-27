from django.conf.urls import url
from Estimates import views

urlpatterns = [
    url(r'^estimate/$', views.EstimateApi),
    url(r'^estimate/([0-9])$', views.EstimateApi),
]