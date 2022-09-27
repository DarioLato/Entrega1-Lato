from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre,self.apellido)

class Artista(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    estilo = models.CharField(max_length=40)

    def __Str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre,self.apellido)

class Tattoos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=40)
    nombre_artista = models.CharField(max_length=40)
    apellido_cliente = models.CharField(max_length=40)
    fecha_tat = models.DateField()
    estilo_tat = models.CharField(max_length=200)
    lugar_tat = models.CharField(max_length=200)

    def __Str__(self):
        texto = "{0} {1} {5} {7}"
        return texto.format(self.nombre_cliente,self.nombre_artista, self.fecha_tat, self.lugar_tat)


