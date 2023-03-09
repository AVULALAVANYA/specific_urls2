from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ammu(request):
    return HttpResponse('she is very closed to me')

def chrome(request):
    return HttpResponse('u can search for anything')
