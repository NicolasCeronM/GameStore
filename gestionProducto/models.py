from django.db import models

# Create your models here.

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="productos",null=True)
    trailer = models.URLField(max_length=200, null=True)
    precio = models.IntegerField()
    detalle = models.TextField()
    plataforma = models.ForeignKey(Plataforma, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
