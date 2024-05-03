from django.shortcuts import render, redirect
from .forms import TurnosForm
from .models import Turnos
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def home_view(request):
    return render(request, "turno/home.html")


def reservar_turno(request):
    if request.method == 'POST':
        form = TurnosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_turnos')
    else:
        form = TurnosForm()
    return render(request, 'turnos/reservar_turno.html', {'form': form})

def lista_turnos(request):
    turnos = Turnos.objects.all()
    return render(request, 'turnos/lista_turnos.html', {'turnos': turnos})

def crear_turno(request):
    if request.method == 'POST':
        form = TurnosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_turnos')
    else:
        form = TurnosForm()
    return render(request, 'turnos/crear_turno.html', {'form': form})


def borrar_turno(request, turno_id):
    turno = Turnos.objects.get(pk=turno_id)
    turno.delete()
    return redirect('lista_turnos')


def editar_turno(request, turno_id):
    turno = Turnos.objects.get(pk=turno_id)
    if request.method == 'POST':
        form = TurnosForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('lista_turnos')
    else:
        form = TurnosForm(instance=turno)
    return render(request, 'turnos/editar_turno.html', {'form': form})

def search_turno_view(request, nombre_de_usuario):
    reservas_turnos = Turnos.objects.filter(
        nombre_de_usuario=nombre_de_usuario
    ).all()
    contexto_dict = {"reservas_de_turnos": reservas_turnos}
    return render(request, "turnos/lista_turnos.html", contexto_dict)


def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "turnos/login.html", {"form": form})

def user_logout_view(request):
    logout(request)
    return redirect("login")

def about(request):
    return render(request, 'about.html')