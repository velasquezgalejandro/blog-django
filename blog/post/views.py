from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator

from .models import  Post
from .forms import  PostModelForm

# Create your views here.
def post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post': post})

def inicio(request):
    pass
    return render(request, 'inicio.html')

def listar_post(request):
    posts_list = Post.objects.all()
    query = request.GET.get('q')
    paginator = Paginator(posts_list, 10)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    # if precio_min and precio_max:
    #     posts_list = posts_list.filter(precio__gte = precio_min, precio__lte= precio_max)

    if query:
        posts_list = posts_list.filter(Q(titulo__icontains = query)| Q(contenido__icontains = query) | Q(categoria__icontains = query))
    return render(request, 'listar_post.html', {'posts': posts})

def agregar_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostModelForm
    return render(request, 'agregar_post.html', {'form': form})
