from tabnanny import verbose
from django.db import models
import datetime

# Create your models here.
class Empleos_Categoria(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    categoria = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False)
    fecha = models.DateTimeField(default=datetime.datetime.today, blank = False, null = False) # o podemos poner Date
    descripcion = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    experiencia = models.TextField(blank=False, null=False)
    funciones = models.TextField(blank=True, null=True)
    ofertas = models.TextField(blank=True, null=True)
    requerimientos = models.TextField(blank=False, null=False)
    detalles_autor = models.TextField(blank=True, null=True)
    sueldo = models.FloatField(blank= False,null=False)
    contrato = models.CharField(max_length=100, blank=False)
    informacion_empresa = models.TextField(blank=False, null=False)

    def __str__(self):      #para nombrar el campo principal
        return self.categoria


       # class Meta: 
            #verbose_name =  ("Products")
            #verbose_name = ("Products dell") - ->

""" class Empleos_Ciudad(models.Model):
    ciudad = models.CharField(max_length=100, blank=False, null=False)
    empleos_en = models.CharField(max_length=100, blank=True, null=True)
    autor = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False)
    fecha = models.DateTimeField(default=datetime.datetime.today, blank = False, null = False) 
    descripcion = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    experiencia = models.TextField(blank=False, null=False)
    funciones = models.TextField(blank=True, null=True)
    ofertas = models.TextField(blank=False, null=False)
    requerimientos = models.TextField(blank=False, null=False)
    detalles_autor = models.TextField(blank=True, null=True)
    sueldo = models.FloatField(blank= False,null=False)
    contrato = models.CharField(max_length=100, blank=False)
    informacion_empresa = models.TextField(blank=False, null=False)

    def __str__(self):      
        return self.ciudad """

""" class Empleos_Estado_Federal(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False)
    fecha = models.DateTimeField(default=datetime.datetime.today, blank = False, null = False) # o podemos poner Date
    descripcion = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    experiencia = models.TextField(blank=False, null=False)
    funciones = models.TextField(blank=True, null=True)
    ofertas = models.TextField(blank=True, null=True)
    requerimientos = models.TextField(blank=False, null=False)
    detalles_autor = models.TextField(blank=True, null=True)
    sueldo = models.FloatField(blank= False,null=False)
    contrato = models.CharField(max_length=100, blank=False)
    informacion_empresa = models.TextField(blank=False, null=False)

    def __str__(self):      
        return self.estado """
    
class Empleos_Cargo_Profesional(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    cargo_profesional = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False)
    fecha = models.DateTimeField(default=datetime.datetime.today, blank = False, null = False) # o podemos poner Date
    descripcion = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    experiencia = models.TextField(blank=True, null=True)
    funciones = models.TextField(blank=True, null=True)
    ofertas = models.TextField(blank=False, null=False)
    requerimientos = models.TextField(blank=False, null=False)
    detalles_autor = models.TextField(blank=True, null=True)
    sueldo = models.FloatField(blank= False,null=False)
    contrato = models.CharField(max_length=100, blank=False)
    informacion_empresa = models.TextField(blank=False, null=False)

    def __str__(self):      #para nombrar el campo principal
        return self.cargo_profesional


class Servicios(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.titulo

class Orienta(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    subtitulo = models.CharField(max_length=100, blank=False, null=True)
    descripcion = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.titulo





""" class Empleos_Sueldo(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=100, blank=False, null=False)
    informacion = models.TextField(blank=False, null=False)
    salario = models.FloatField(blank= False,null=False)
    media_salarial = models.FloatField(blank= True,null=True)
    salarios_relacionados = models.FloatField(blank= False,null=False)
    empresas_populares = models.TextField(blank=False, null=False)
    categoria = models.TextField(blank=False, null=False)
    
    

    def __str__(self):      
        return self.salario """

""" class Empleos_Localizacion(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    empresa = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    experiencia = models.TextField(blank=True, null=True)
    funciones = models.TextField(blank=True, null=True)
    requerimientos = models.TextField(blank=False, null=False)
    sueldo = models.FloatField(blank= False,null=False)
    contrato = models.CharField(max_length=100, blank=False)
    ofertas_similares = models.TextField(blank=False, null=False)

    def __str__(self):      
        return self.empresa """

class Empresas_Industria (models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    industria = models.CharField(max_length=100, blank=False, null=False)
    fecha = models.DateTimeField(default=datetime.datetime.today, blank = False, null = False) # o podemos poner Date
    descripcion = models.TextField(blank=False, null=False)
    requisitos = models.TextField(blank=False, null=False)
    funciones = models.TextField(blank=False, null=False)
    ofertas = models.TextField(blank=True, null=True)
    requerimientos = models.TextField(blank=False, null=False)
    sueldo = models.FloatField(blank= False,null=False)
    contrato = models.CharField(max_length=100, blank=False)
    informacion_empresa = models.TextField(blank=False, null=False)

    def __str__(self):      #para nombrar el campo principal
        return self.industria

class Comentarios(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    correo_electronico = models.EmailField(max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=100, blank=False, null=False)
    mensaje = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = ("mensaje")
        verbose_name_plural = ("mensajes")

    def __str__(self):      #para nombrar el campo principal
        return self.nombre
