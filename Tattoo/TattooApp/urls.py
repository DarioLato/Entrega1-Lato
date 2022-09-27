from django.contrib import admin
from django.urls import path
from django.urls import include
from TattooApp.views import *
from TattooApp import views

urlpatterns = [
    path('inicio/', inicio),
    path('clientes', clientes),
    path('artistas', artistas),
    path('historia', historia),
    path('form_clientes', views.clienteFormulario),
    path('form_artista', views.artistaFormulario),
    path('form_tattoo', views.tattooFormulario),
    path('buscar_tattoo', buscar_tattoo),
    path('buscar', views.buscar),

]