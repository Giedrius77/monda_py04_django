# kuriame nauja front end view vietoj raketos

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
]