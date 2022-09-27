from django.shortcuts import render
from TattooApp.forms import *
from TattooApp.models import Cliente, Artista, Tattoos
from django.http import HttpResponse

def inicio(request):
    return render(request, "TattooApp/inicio.html")

def clientes(request):

    cliente = Cliente.objects.all()
    return render(request, "TattooApp/clientes.html", {"clientes": cliente})

def artistas(request):

    artista = Artista.objects.all()
    return render(request, "TattooApp/artistas.html", {"artistas": artista})

def historia(request):
    tattoos = Tattoos.objects.all()
    return render(request, "TattooApp/historia.html", {"tattoos": tattoos})


def clienteFormulario(request):
    if request.method == "POST":
        formulario = form_cliente(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], 
            direccion=informacion['direccion'], ciudad=informacion['ciudad'], email=informacion['email'])
            cliente.save()
            return render(request, "TattooApp/inicio.html")
    else:
        formulario=form_cliente()
    return render(request, "TattooApp/form_clientes.html", {"formulario": formulario})


def artistaFormulario(request):
    if request.method == "POST":
        formulario = form_artista(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            artista = Artista(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], 
            direccion=informacion['direccion'], ciudad=informacion['ciudad'], estilo=informacion['estilo'])
            artista.save()
            return render(request, "TattooApp/inicio.html")
    else:
        formulario=form_artista()
    return render(request, "TattooApp/form_artista.html", {"formulario": formulario})

def tattooFormulario(request):
    if request.method == "POST":
        formulario = form_tattoos(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            tattoo = Tattoos(id=informacion['id'], nombre_cliente=informacion['nombre_cliente'], nombre_artista=informacion['nombre_artista'], 
            apellido_cliente=informacion['apellido_cliente'], fecha_tat=informacion['fecha_tat'], estilo_tat=informacion['estilo_tat'], lugar_tat=informacion['lugar_tat'])
            tattoo.save()
            return render(request, "TattooApp/inicio.html")
    else:
        formulario=form_tattoos()
    return render(request, "TattooApp/form_tattoo.html", {"formulario": formulario})


def buscar_tattoo(request):

    return render(request, "TattooApp/buscar_tattoo.html")


def buscar(request):
    if request.GET["id"]:
        id = request.GET["id"]
        tattoos = Tattoos.objects.filter(id__icontains = id)
        return render(request, "TattooApp/resultado_busqueda.html", {"tattoos":tattoos, "id":id})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

