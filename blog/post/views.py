from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime

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
    fecha_min_str = request.GET.get('fecha_min')
    fecha_max_str = request.GET.get('fecha_max')

    try:
        if fecha_min_str:
            fecha_min = datetime.strptime(fecha_min_str, '%d/%m/%Y').date()
        else:
            fecha_min = None

        if fecha_max_str:
            fecha_max = datetime.strptime(fecha_max_str, '%d/%m/%Y').date()
        else:
            fecha_max = None
    except ValueError:
        fecha_min = None
        fecha_max = None

    if fecha_min and fecha_max:
        if fecha_min <= fecha_max:
            posts_list = posts_list.filter(
                fecha_publicacion__gte=fecha_min,
                fecha_publicacion__lte=fecha_max
            )
        else:
            posts_list = posts_list.none()
    elif fecha_min:
        posts_list = posts_list.filter(fecha_publicacion__gte=fecha_min)
    elif fecha_max:
        posts_list = posts_list.filter(fecha_publicacion__lte=fecha_max)

    if query:
        posts_list = posts_list.filter(Q(titulo__icontains = query) | Q(contenido__icontains = query) | Q(categoria__icontains = query))

    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

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

def editar_post(request, pk):
    post= Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listar_post')
    else:
        form = PostModelForm(instance=post)
    return render(request, 'editar_post.html', {'form': form})

def detalle_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'detalle_post.html', {'post': post})
