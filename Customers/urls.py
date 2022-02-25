from django.conf.urls import url
from Customers import views

urlpatterns = [
    url(r'^customer/$', views.customerApi),
    url(r'^customer/([0-9])$', views.customerApi),
]