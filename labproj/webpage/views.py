from django.shortcuts import render

# Create your views here.

def webpage_view(request):
    context = {
        "Name": "Shahad",
        "Major": "mis",
        "Courses_List": ["mis", "finanace", "e-commerce", "acc1"],
        "Courses_Grades": [
            {"Course": "mis",          "Grade":"B"},
            {"Course": "finance",      "Grade":"B+"},
            {"Course": "e-commerce",   "Grade":"A"},
            {"Course": "acc1",         "Grade":"A"}
        ]
    }
    
    return render(request, 'shahad.html', context)



