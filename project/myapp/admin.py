from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Autor, Libro

admin.site.register(Autor)
admin.site.register(Libro)
