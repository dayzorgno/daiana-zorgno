from django.urls import path
from . import views 
from . views import (home_view, user_login_view, user_logout_view, search_turno_view,)

urlpatterns = [
    path("", home_view),
    path('reservar/', views.reservar_turno, name='reservar_turno'),
    path('lista/', views.lista_turnos, name='lista_turnos'),
    path('crear/', views.crear_turno, name='crear_turno'),
    path('editar/<int:turno_id>/', views.editar_turno, name='editar_turno'),
    path('borrar/<int:turno_id>/', views.borrar_turno, name='borrar_turno'),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path('buscar/<str:nombre_de_usuario>/', search_turno_view, name='buscar_turno'),
    path('about/', views.about, name='about'),
]