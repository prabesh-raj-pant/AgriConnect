
from django.contrib import admin
from django.urls import path
from .views import index,pricing,fertilizerCalculator

urlpatterns = [
    path('',index),
    path('index',index),
    path('fertilizerCalculator',fertilizerCalculator),
    path('pricing',pricing),
    path('admin/', admin.site.urls),
    
]
