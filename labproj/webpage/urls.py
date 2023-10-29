from django.urls import path
from webpage.views import webpage_view

urlpatterns = [
    path('webpage/',webpage_view),
]