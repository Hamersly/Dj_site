from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginFormView.as_view(), name='login_url'),
    path('register', RegisterFormView.as_view(), name='register_url'),
    path('logout', LogoutView.as_view(), name='logout_url'),
]
