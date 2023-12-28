
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('index',index),
    path('fertilizerCalculator',fertilizerCalculator),
    path('weather',weather),
    path('financial',financial),
    path('farmingtechnique',farmingtechnique),
    path('market',market),
    path('hotel',hotel),
    path('pricing',pricing),
    path('admin/', admin.site.urls),
    
]
