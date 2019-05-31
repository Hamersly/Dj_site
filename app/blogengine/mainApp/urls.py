from django.urls import path
from django.urls import include
from .views import *


urlpatterns = [
    # path('', posts_list, name='posts_list_url'),
    # path('posts/<str:slug>/', post_detail, name ='post_detail_url'),
    path('', index, name='index'),
]