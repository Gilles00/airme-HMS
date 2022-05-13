from django.urls import re_path as url
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import AuthenticationForm

app_name = 'accounts'

urlpatterns = [
    url(r'^login$', LoginView.as_view(), {
            'template_name': 'accounts/login.html',
            'authentication_form': AuthenticationForm
        },
        name='login'
    ),
    url(r'^logout/$', LogoutView.as_view(), {'login_url':'accounts:login'}, name='logout'),
]
