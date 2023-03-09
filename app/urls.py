from app.views import *
from django.urls import path
app_name='know'
urlpatterns=[
    path('ammu/',ammu,name='ammu'),
    path('chrome/',chrome,name='chrome'),
]