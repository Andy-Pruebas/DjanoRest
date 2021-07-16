from django.db import models

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_autor

class Libro(models.Model):
    codigo = models.IntegerField()
    titulo = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    editorial = models.CharField(max_length=50)
    numpags = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.titulo,self.autor)

class Usuario(models.Model):
    NumUsuario = models.IntegerField()
    NIF = models.CharField(max_length=20)
    nombre_usuario = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)

    def __str__(self):
        return "{} - {}".format(self.nombre_usuario,self.NIF)

class Prestamos(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE,)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
    fecPrestamo = models.DateField()
    fecDevolucion = models.DateField()

    def __str__(self):
        return "{0} ({1})".format(self.libro, self.usuario)


