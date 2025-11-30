from django.db import models

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre