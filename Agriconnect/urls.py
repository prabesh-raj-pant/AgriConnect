
from django.contrib import admin
from django.urls import path
from .views import index,pricing

urlpatterns = [
    path('',index),
    path('index',index),
    path('pricing',pricing),
    path('admin/', admin.site.urls),
    
]
