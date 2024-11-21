from django.contrib import admin
from App import models
from .models import Proyecto

# Register your models here.
class AdmProyecto(admin.ModelAdmin):
    list_display=('nombreproyecto','descripcion','imagen','tecnologias','estado')

admin.site.register(Proyecto,AdmProyecto)

