from django.conf.urls import url
from Invoice import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^invoice/$', views.invoiceApi),
    url(r'^invoice/([0-9]+)$', views.invoiceApi),
]