from django.conf.urls import url
from Vendors import views

urlpatterns = [
    url(r'^vendor/$', views.vendorApi),
    url(r'^vendor/([0-9])$', views.vendorApi),
]