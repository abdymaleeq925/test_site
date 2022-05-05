from django.urls import path

from .views import greetings
urlpatterns = [
    path('', greetings, name='greetings'),
]