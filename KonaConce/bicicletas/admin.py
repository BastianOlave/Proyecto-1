from django.contrib import admin
# Importamos los 3 modelos
from .models import Bike, Categoria, Marca

# --- Registro para Categoria ---
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Admin para el modelo Categoria."""
    list_display = ("name",)
    search_fields = ("name",)

# --- Registro para Marca ---
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    """Admin para el modelo Marca."""
    list_display = ("name",)
    search_fields = ("name",)

# --- Registro personalizado para Bike (Cumple Punto 2) ---
@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    """Admin personalizado para el modelo Bike."""
    
    # --- 1. list_display: Qué columnas mostrar en la lista ---
    # Añadimos marca y categoría a la vista
    list_display = ("name", "marca", "categoria", "price", "stock", "updated")
    
    # --- 2. list_filter: Qué filtros mostrar en la barra lateral ---
    # Añadimos filtros por marca y categoría
    list_filter = ("stock", "marca", "categoria", "created", "updated")
    
    # --- 3. search_fields: Por qué campos buscar ---
    # Permitimos buscar por el nombre de la marca/categoría (usando __name)
    search_fields = ("name", "marca__name", "categoria__name")
    
    # --- 4. list_editable: Campos editables directamente en la lista ---
    # (¡Estos campos DEBEN estar también en list_display!)
    list_editable = ("price", "stock")
    
    # --- 5. raw_id_fields: Mejora el rendimiento para Claves Foráneas ---
    # (Reemplaza el <select> por un campo de búsqueda cuando hay muchos)
    raw_id_fields = ("marca", "categoria")
    
    # --- 6. readonly_fields: Campos que no se pueden editar ---
    # (Útil para campos automáticos como created/updated)
    readonly_fields = ("created", "updated")
    
    # --- 7. fieldsets: Organiza la vista de detalle en secciones ---
    # (Esto organiza el formulario cuando creas/editas una Bici)
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