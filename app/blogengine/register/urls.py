from django.urls import path
from .views import *

urlpatterns = [
    path('', RegisterFormView.as_view(), name='register_url'),
    path('login', LoginFormView.as_view(), name='login_url'),
]
