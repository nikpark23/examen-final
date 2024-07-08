from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'radiojugoso/index.html')

def noticias(request):
    return render(request, 'radiojugoso/noticias.html')

def galeria(request):
    return render(request, 'radiojugoso/galeria.html')

def tienda(request):
    return render(request, 'radiojugoso/tienda.html')

def contacto(request):
    return render(request, 'radiojugoso/contacto.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {username}')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return redirect('index')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Cuenta creada para {user.username}')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'radiojugoso/register.html', {'form': form})


def index(request):
    return render(request, 'radiojugoso/index.html')

def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'radiojugoso/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UserCreationForm()
    return render(request, 'radiojugoso/usuario_form.html', {'form': form})

def editar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UserChangeForm(instance=usuario)
    return render(request, 'radiojugoso/usuario_form.html', {'form': form})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'radiojugoso/usuario_confirm_delete.html', {'usuario': usuario})