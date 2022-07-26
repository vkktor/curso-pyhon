from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# index(request) é convenção


def index(request):
    return HttpResponse('Olá Mundo!')
