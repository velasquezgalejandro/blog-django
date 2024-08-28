from django.urls import path
from .views import post, agregar_post, listar_post

urlpatterns = [
    path('post/', post, name='post'),
    path('agregar_post/', agregar_post, name='agregar_post'),
    path('listar_post/', listar_post, name='listar_post'),
]
