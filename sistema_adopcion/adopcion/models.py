from django.db import models

# Create your models here.

from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estado_salud = models.CharField(max_length=100)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=50)

class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    preferencias = models.TextField()
    historial_adopciones = models.ManyToManyField(Perro, blank=True)