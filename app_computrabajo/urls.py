
from django.urls import path
from .views import index, buscar, entornodigital, liderazgo, multigeneracional, discapacidad, contacto, servicios, proyectos, vacantes
from django.conf import settings
from django.conf.urls.static import static

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
    
]
urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
