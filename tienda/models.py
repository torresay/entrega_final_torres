from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):

    marca = models.CharField(max_length=40)
    pais  = models.CharField(max_length=15)
    ano_origen = models.IntegerField()
    contacto = models.EmailField()
    imagen = models.ImageField(upload_to='marcas/', null=True, blank=True)

    def __str__(self,):
        return str(self.marca)


class Cartera(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
    precio = models.FloatField()
    color = models.CharField(max_length=15)
    dimensiones = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='carteras/', null=True, blank=True)

    def __str__(self,):
        return str(self.modelo)


class Zapato(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
    precio = models.FloatField()
    color = models.CharField(max_length=15)
    dimensiones = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='zapatos/', null=True, blank=True)

    def __str__(self,):
        return str(self.modelo)


# class CustomUser(AbstractUser):
#     image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
#     groups = models.ManyToManyField(
#         to='auth.Group',
#         related_name='custom_user_groups',
#         blank=True,
#         help_text='Los grupos a los que pertenece el usuario. Un usuario puede ser miembro de cero o más grupos.'
#     )
#     user_permissions = models.ManyToManyField(
#         to='auth.Permission',
#         related_name='custom_user_user_permissions',
#         blank=True,
#         help_text='Los permisos específicos del usuario.'
#     )

class DataUser(models.Model):
    user = models.OneToOneField(User,blank=False,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.user.username