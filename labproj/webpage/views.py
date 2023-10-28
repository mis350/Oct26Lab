from django.shortcuts import render

# Create your views here.
def webpage_view(request):

    
        data = {} 
        data["name"] = "Mohammed"
        data["team1"] = "Ali"
        data["team2"] = "Saad"



    
        return render (request, 'mohammed.html', context=data)