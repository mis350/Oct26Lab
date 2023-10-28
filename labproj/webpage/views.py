from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def webpage_view(request):
    c = {
        "name" : request.GET.get("name",""),
        "age" : "24",
        "classes" : ["python","Java","Html"]



    }
    return render (request, 'Naser.html', c )