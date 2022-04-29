
from django.urls import path
from .views import index, buscar, entornodigital, liderazgo, multigeneracional, discapacidad, contacto, servicios, proyectos, vacantes, Registro, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from .forms import loginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', index, name='inicio'),
    path('buscar/', buscar, name='buscar'),
    path('contacto', contacto, name='contacto'),
    path('servicios/', servicios, name='servicios'),
    path('vacantes/', vacantes, name='vacantes'),
    path('entornodigital/', entornodigital, name='entornodigital'),
    path('liderazgo/', liderazgo, name='liderazgo'),
    path('discapacidad/', discapacidad, name='discapacidad'),
    path('proyectos/', proyectos, name='proyectos'),
    path('multigeneracional/', multigeneracional, name='multigeneracional'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='app/login.html', authentication_form=loginForm), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    
]
urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
