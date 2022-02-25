from django.conf.urls import url
from Expenses import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^expense/$', views.ExpenseApi),
    url(r'^expense/([0-9]+)$', views.ExpenseApi),
]