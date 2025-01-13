from django.shortcuts import render
from  django.http import HttpResponse

def index(request):
    response = HttpResponse('<h1> Home </h1>')
    return response
