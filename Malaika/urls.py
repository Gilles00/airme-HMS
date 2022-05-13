"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
# openapi.Info(
# title="KISIIZI HOSPITAL API",
# default_version='v1',
# description="Test description",
# terms_of_service="https://www.myapp.com/policies/terms/",
# contact=openapi.Contact(email="contact@kisiiziug.local"),
# license=openapi.License(name="Test License"),
# ),
# public=True,
# permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('accounts.urls')),
    url(r'^', include('hospital.urls')),
    url(r'^', include('operations.urls')),
    url(r'^', include('staff.urls')),
    url(r'^', include('finance.urls')),
    url(r'^', include('reception.urls')),
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),name='schema-json'),
    # url('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url('^redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
