from django import forms
from .models import Turnos 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render


class TurnosForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['tipo_de_servicio', 'tipo_de_turno', 'fecha', 'horario_disponible', 'nombre_de_usuario']


class Search_Turno_View(LoginRequiredMixin, View):
    def get(self, request, nombre_de_usuario):
        reservas_turnos = Turnos.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        contexto_dict = {"reservas_de_turnos": reservas_turnos}
        return render(request, "turnos/lista_turnos.html", contexto_dict)