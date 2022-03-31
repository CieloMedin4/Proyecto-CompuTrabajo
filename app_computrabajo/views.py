from ast import If
from urllib import request
from django.shortcuts import render
from .models import Empleos_Cargo_Profesional, Servicios, Orienta
from .forms import ComentariosForm

# Create your views here.
def index(request):
    ori = Orienta.objects.all()
    datos = {
        "orienta" : ori
    }
    return render(request, 'app/index.html', datos)
def entornodigital(request):
    return render(request, 'app/entornodigital.html')
def liderazgo(request):
    return render(request, 'app/liderazgo.html')
def discapacidad(request):
    return render(request, 'app/discapacidad.html')
def multigeneracional(request):
    return render(request, 'app/multigeneracional.html')


def contacto(request):
    datos = {
        "form": ComentariosForm
    }
    if request.method == 'POST':
        formulario = ComentariosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["form"] = formulario
    return render(request, 'app/contacto.html', datos)


def servicios(request):
    ser = Servicios.objects.all()
    datos = {
        "Servicio" : ser
        }
    return render(request, 'app/servicios.html', datos)

def proyectos(request):
    return render(request, 'app/proyectos.html')

def vacantes(request):
    Cargo_Profesional = Empleos_Cargo_Profesional.objects.all()
    datos = {
        "Cargo_Profesional" : Cargo_Profesional
        }
    return render(request, 'app/vacantes.html', datos)
    

def buscar(request):
    if request.GET['busqueda']:
        query = request.GET['busqueda']
        cargos = Empleos_Cargo_Profesional.objects.filter(titulo__icontains=query)
        orienta = Orienta.objects.filter(titulo__icontains=query)
        service = Servicios.objects.filter(titulo__icontains=query)

        datos = {
            "resultados" : cargos,
            "orien" : orienta,
            "servicio" : service,
            "query" : query
        }
        return render(request, 'app/buscar.html', datos)
    else:
        return render(request, 'app/buscar.html')