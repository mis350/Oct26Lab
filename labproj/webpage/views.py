from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def webpage_view(request):
    c = {
        "age" : "24"


    }
    return render (request, 'Naser.html', c )