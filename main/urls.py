from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cars/', cars, name='cars'),
    path('services/', services, name='services'),
    path('contacts/', contacts, name='contacts'),
]