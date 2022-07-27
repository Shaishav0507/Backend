from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf.urls import url, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin

schema_view = get_schema_view(
   openapi.Info(
      title="TaxRx API Documentation",
      default_version='v1',
      description="TaxRx",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@psyber.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/',admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    url(r'^', include('start.urls')),
    url(r'^', include('Invoice.urls')),
    url(r'^', include('Vendors.urls')),
    url(r'^', include('Customers.urls')),
    url(r'^', include('Expenses.urls')),
    url(r'^', include('GSTForm.urls')),
    url(r'^', include('Estimates.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]