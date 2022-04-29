from ast import If
from urllib import request
from django.shortcuts import render, redirect
from .models import Empleos_Cargo_Profesional, Servicios, Orienta, Comentarios, Empresas_Industria
from .forms import ComentariosForm, userForm, loginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView


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


def comentarios(request):
    com = Comentarios.objects.all()
    datos = {
        "Comentario" : com
        }
    return render(request, 'app/contacto.html', datos)

def servicios(request):
    ser = Servicios.objects.all()
    datos = {
        "Servicio" : ser
        }
    return render(request, 'app/servicios.html', datos)

def proyectos(request):
    Industria = Empresas_Industria.objects.all()
    datos = {
        "Industrias" : Industria
    }
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


class Registro(View):
    form_class = userForm
    initial = {'key': 'value'}
    template_name = 'app/registro.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')
        #else process dispatch as it otherwise normally would
        return super(Registro, self).dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView):
    form_class = loginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get ('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser in closed.
            self.request.session.set_expiry(0)
            # set session as modified to force data updates/cookie to be saved
            self.request.session.modified = True
        #else browser session whill be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py.
        return super(CustomLoginView, self).form_valid(form)