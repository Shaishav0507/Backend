from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf.urls import url, include

urlpatterns = [
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    url(r'^', include('start.urls')),
    url(r'^', include('Invoice.urls')),
    url(r'^', include('Vendors.urls')),
    url(r'^', include('Customers.urls')),
    url(r'^', include('Expenses.urls')),
    url(r'^', include('GSTForm.urls'))
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
