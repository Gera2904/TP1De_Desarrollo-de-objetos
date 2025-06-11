from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Perro, UsuarioAdoptante

admin.site.register(Perro)
admin.site.register(UsuarioAdoptante)

