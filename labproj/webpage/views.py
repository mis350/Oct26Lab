from django.shortcuts import render

# Create your views here.
def webpage_view(request):

    context = {
        "name": request.GET.get("name", ""),
        "major": "Mis",
        "gpa": 4.0,
        "students": ["rawan", "abrar", "fatemah", "noor"],

    }

    return render (request, 'rawan.html', context)
