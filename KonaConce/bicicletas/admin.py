from django.contrib import admin
from .models import Bike, Categoria, Marca

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Admin para el modelo Categoria."""
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    """Admin para el modelo Marca."""
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    """Admin personalizado para el modelo Bike."""
    
    list_display = ("name", "marca", "categoria", "price", "stock", "updated")
    list_filter = ("stock", "marca", "categoria", "created", "updated")
    search_fields = ("name", "marca__name", "categoria__name")
    list_editable = ("price", "stock")
    raw_id_fields = ("marca", "categoria")
    readonly_fields = ("created", "updated")
    fieldsets = (
        (None, {
            "fields": ("name", "image")
        }),
        ("Relaciones (Obligatorio)", {
            "fields": ("marca", "categoria")
        }),
        ("Detalles de Venta", {
            "fields": ("description", "price", "stock")
        }),
        ("Timestamps (Automático)", {
            "fields": ("created", "updated")
        }),
    )