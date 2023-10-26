from django.shortcuts import render


# Create your views here.
def webpage_view(request):
    
    return render (request, 'maida.html')