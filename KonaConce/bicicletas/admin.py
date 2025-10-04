from django.contrib import admin
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "created", "updated")
    search_fields = ("name",)
    list_filter = ("stock", "created")
