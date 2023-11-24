from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from    .models import *
# Create your views here.

#modelo copy
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('nombre_de_la_vista')  #agregar nombre de la vista
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


def index(request):
    return render(request, 'Aplicacion/index.html')

def base(request):
    return render (request, "Aplicacion/base.html")

def registro(request):
    return render (request, "Aplicacion/registro.html")

def home(request):
    return render(request, 'Aplicacion/home.html')

def about_me(request):
    return render(request, 'Aplicacion/about_me.html')

def post(request):
    return render(request, 'Aplicacion/post.html')

def admin_view(request):
    return render(request, "Aplicacion/admin_view")

def post_detail(request, post_id):
    # Obtener el post específico según su ID
    post = Post.objects.get(id=post_id)
    return render(request, 'Aplicacion/post_detail.html', {'post': post})




