from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def webpage_view(request):
    data = {"name": request.GET.get("name"," "),
            "major":request.GET.get("major"," "),
            "courses":["Micro","acc1","qmis","finance","management"]
    }
    
    return render(request, "duha.html", context=data)