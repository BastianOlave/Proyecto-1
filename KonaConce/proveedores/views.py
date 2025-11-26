from django.shortcuts import render
import requests

def ver_accesorios_externos(request):
    url_api = 'http://127.0.0.1:8001/api/accesorios/'
    
    data = []
    
    try:
        response = requests.get(url_api)
        if response.status_code == 200:
            data = response.json() 
    except:
        print("Error: No se pudo conectar a la API. ¿Está corriendo en el puerto 8001?")

    return render(request, 'proveedores/lista_externa.html', {'accesorios': data})