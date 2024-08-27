from django.urls import path
from .views import post, agregar_post

urlpatterns = [
    path('post/', post, name='post'),
    path('agregar_post/', agregar_post, name='agregar_post'),
]
