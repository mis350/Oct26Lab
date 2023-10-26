from django.shortcuts import render


# Create your views here.
def webpage_view(request):
    data = {}
    data['abdullah'] = 'abady'
    return render (request, 'abdullah.html', context=data)