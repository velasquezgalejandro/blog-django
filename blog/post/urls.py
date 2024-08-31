from django.urls import path
from .views import post, agregar_post, listar_post, editar_post, detalle_post

urlpatterns = [
    path('post/', post, name='post'),
    path('agregar_post/', agregar_post, name='agregar_post'),
    path('editar_post/<int:pk>/', editar_post, name='editar_post'),
    path('listar_post/', listar_post, name='listar_post'),
    path('post/<int:pk>/', detalle_post, name='detalle_post'),
]
