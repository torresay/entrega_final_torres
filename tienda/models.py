from django.db import models

# Create your models here.
class Marca(models.Model):

    marca = models.CharField(max_length=40)
    pais  = models.CharField(max_length=15)
    ano_origen = models.IntegerField()
    contacto = models.EmailField()


class Producto(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
    precio = models.FloatField()
    color = models.CharField(max_length=15)
    dimensiones = models.CharField(max_length=15)


class Usuario(models.Model):

    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
    email = models.EmailField()
    domicilio = models.CharField(max_length=40)
    telefono = models.IntegerField()
    carteras = models.ForeignKey(Producto, on_delete=models.CASCADE)
    