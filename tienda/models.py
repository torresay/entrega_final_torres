from django.db import models

# Create your models here.
class Marca(models.Model):

    marca = models.CharField(max_length=40)
    pais  = models.CharField(max_length=15)
    ano_origen = models.IntegerField()
    contacto = models.EmailField()

    def __str__(self,):
        return str(self.marca)


class Cartera(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
    precio = models.FloatField()
    color = models.CharField(max_length=15)
    dimensiones = models.CharField(max_length=15)

    def __str__(self,):
        return str(self.modelo)


class Zapato(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
    precio = models.FloatField()
    color = models.CharField(max_length=15)
    dimensiones = models.CharField(max_length=15)

    def __str__(self,):
        return str(self.modelo)
    