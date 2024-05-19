from django.urls import path

from main.views import index, crm_home

urlpatterns = [
    path('', index),
    path('home/', crm_home, name='home')
]
