from rest_framework import serializers
from .models import Prestamos, Usuario, Libro, Autor


class libroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    libro = libroSerializer(read_only=True)
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Prestamos
        fields = ('id', 'libro', 'usuario', 'fecPrestamo', 'fecDevolucion')



