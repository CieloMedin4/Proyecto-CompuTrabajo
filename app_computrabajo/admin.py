from django.contrib import admin
from .models import Empleos_Cargo_Profesional, Empleos_Categoria, Empresas_Industria, Servicios, Orienta, Comentarios

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display =["titulo", "direccion"]
    list_editable = ["direccion"]
    search_fields = ["titulo", "cargo_profesional", "direccion", "fecha"]
    list_per_page = 10

class ServicesAdmin(admin.ModelAdmin):
    list_display =["titulo", "descripcion"]
    list_editable = ["descripcion"]
    search_fields = ["titulo"]
    list_per_page = 10

class OrientaAdmin(admin.ModelAdmin):
    list_display =["titulo", "descripcion", "subtitulo"]
    list_editable = ["descripcion"]
    search_fields = ["titulo"]
    list_per_page = 10

class ComentariosAdmin(admin.ModelAdmin):
    list_display =["nombre", "correo_electronico", "telefono", "mensaje"]
    list_editable = ["mensaje"]
    search_fields = ["correo_electronico"]
    list_per_page = 10

admin.site.register(Empleos_Cargo_Profesional, ProductAdmin)
admin.site.register(Servicios, ServicesAdmin)
admin.site.register(Orienta, OrientaAdmin)
admin.site.register(Empleos_Categoria)
# admin.site.register(Empleos_Ciudad)
# admin.site.register(Empleos_Estado_Federal)
# admin.site.register(Empleos_Localizacion)
# admin.site.register(Empleos_Sueldo)
admin.site.register(Empresas_Industria)
admin.site.register(Comentarios)