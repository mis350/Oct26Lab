from django.urls import path
from webpage.views import webpage_view

urlpatterns = [
    path('web/',webpage_view),
]