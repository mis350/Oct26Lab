from django.shortcuts import render

# Create your views here.
def webpage_view(request):
    
    context = {
        " name " : "Bader" , 
        " Classes" : " MIS350"
    
    }
    
    return render (request, 'Bader.html', context)
