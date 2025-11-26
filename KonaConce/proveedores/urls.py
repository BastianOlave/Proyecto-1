from django.urls import path
from .views import ver_accesorios_externos

urlpatterns = [
    path('ofertas-externas/', ver_accesorios_externos, name='lista_externa'),
]