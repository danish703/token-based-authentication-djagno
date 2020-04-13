from django.urls import path
from account.api.views import (
registration_view,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name='account'
urlpatterns =[
    path('register/',registration_view,name='register_api'),
    path('login/',obtain_auth_token,name='login')
]