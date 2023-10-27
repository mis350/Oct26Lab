from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def webpage_view(request):

    context = {
        "name" : request.GET.get("name"," "),
        "majors": ["MIS", "Accounting", " Operation management ", "Economic"],
        

    }

    return render (request, 'nourah.html', context )