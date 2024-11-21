from django.db import models

class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('T', 'Terminado'),
    ]
    nombreproyecto = models.CharField(max_length=50)
    descripcion = models.TextField()  
    imagen = models.ImageField(upload_to='proyectos/') 
    tecnologias = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')
    repositorio = models.URLField(blank=True, null=True)  # Campo para el enlace del repositorio

    def __str__(self):
        return self.nombreproyecto

