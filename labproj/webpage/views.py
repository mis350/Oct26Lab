from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def webpage_view(request):
    x = HttpResponse('Hello World')
    return x