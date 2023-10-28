
from django.shortcuts import render
 
# Create your views here.
 
def webpage_view(request):
    context = {
        "Name": "sara",
        "countries_List": ["Kuwait","Qatar","Oman"],
        "countreis_capital": [
            {"countre": "Kuwait",          "capital":"Kuwait Cit"},
            {"Course": "Qatar",      "capital":"Doha"},
            {"Course": "Oman",   "capital":"Muscat"},
        ]
    }
   
    return render(request, 'sara.html', context)