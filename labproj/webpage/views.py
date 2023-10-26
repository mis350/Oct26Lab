from django.shortcuts import render


# Create your views here.
def webpage_view(request):
    context = { "name": "Laila",
               'Classes' : ['mis350','mis130','mis340']
   }
    return render (request, 'laila.html', context)