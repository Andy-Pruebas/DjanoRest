from django.contrib import admin
from Libros.Prestamos.models import *
# Register your models here.

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Prestamos)
