from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def webpage_view(request):
    
    context = {
       # "query": request.GET("query"),
        "name": request.GET.get("name", ""),
        "Classes": ["350","220","106"]
                  
    }
    
    
    return render (request, 'ahmad.html', context)