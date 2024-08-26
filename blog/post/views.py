from django.shortcuts import render, redirect
from .models import  Post

# Create your views here.
def post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post': post})

def inicio(request):
    pass
    return render(request, 'inicio.html')
