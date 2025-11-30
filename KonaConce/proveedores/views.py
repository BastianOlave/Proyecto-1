from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import user_passes_test


def es_admin_o_staff(user):
    return user.is_superuser or user.groups.filter(name='Staff').exists()

@user_passes_test(es_admin_o_staff, login_url='/') 
def ver_accesorios_externos(request):
    url_api = 'http://127.0.0.1:8001/api/accesorios/'
    
    data = []
    
    try:
        response = requests.get(url_api, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar a la API. ¿Está corriendo en el puerto 8001?")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    return render(request, 'proveedores/lista_externa.html', {'accesorios': data})