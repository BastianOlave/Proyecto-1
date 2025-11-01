from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']

    def __str__(self):
        return self.name


class Marca(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['name']

    def __str__(self):
        return self.name

class Bike(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="bikes", verbose_name="Marca")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="bikes", verbose_name="Categoría")
    
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    image = models.ImageField(upload_to="bicicletas/", verbose_name="Imagen")
    stock = models.BooleanField(default=True, verbose_name="En Stock")  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Bicicleta"
        verbose_name_plural = "Bicicletas"
        ordering = ['-created']

    def __str__(self):
        marca_name = self.marca.name if self.marca else "Sin Marca"
        return f"{self.name} ({marca_name})"
