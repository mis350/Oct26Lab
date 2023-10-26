from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def webpage_view(request):
    data = {}
    data["name"] = "Ahmad"
    data["guest"] = "Abdullah"
    #x = HttpResponse('Hello World')
    return render(request, "farid.html", context=data)