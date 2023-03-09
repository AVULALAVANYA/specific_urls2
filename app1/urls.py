from app1.views import *
from django.urls import path
app_name='just'
urlpatterns=[
    path('lavu/',lavu,name='lavu'),
]