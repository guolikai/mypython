from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request,kwargs):
    
    return HttpResponse('app03.index')