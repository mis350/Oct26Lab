from django.shortcuts import render

# Create your views here.

def webpage_view(request):
    context = {
        "name": "Bader",
        "Classe": "MIS350",
        "Professors_List": ["Dr. Ali", "Dr. Mariam", "Dr. Mohammad"],
        "Courses_Grades": [
            {"Course": " MIS 240", "Grade": "B+"},
            {"Course": " MIS 120", "Grade": "B-"},
            {"Course": " Accounting 1", "Grade": "F"}
        ]
    }
    
    return render(request, 'Bader.html', context)
