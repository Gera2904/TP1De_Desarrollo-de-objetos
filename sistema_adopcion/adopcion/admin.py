from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Perro, UsuarioAdoptante, Preferencias

admin.site.register(Perro)
admin.site.register(UsuarioAdoptante)
admin.site.register(Preferencias)