from django.shortcuts import render

# Create your views here.
def webpage_view(request):
    context = { 
    
    "books": ["Deth on the Nile", "Murder on the orient Express", "And then there were none"]

    }
    return render (request, 'abrar.html', context)