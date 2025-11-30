from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .forms import RegistroForm
from bicicletas.models import Bike 

def asignar_grupo_y_permisos(user, nombre_grupo, codenames_permisos):
    group, created = Group.objects.get_or_create(name=nombre_grupo)
    if created:
        content_type = ContentType.objects.get_for_model(Bike)
        for codename in codenames_permisos:
            try:
                permiso = Permission.objects.get(codename=codename, content_type=content_type)
                group.permissions.add(permiso)
            except Permission.DoesNotExist:
                print(f"Permiso {codename} no encontrado.")
        print(f"Grupo '{nombre_grupo}' creado y permisos asignados.")
    
    user.groups.add(group)

def registro_cliente(request):
    if request.user.is_authenticated:
        return redirect('/') 
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            asignar_grupo_y_permisos(user, 'Cliente', ['view_bike'])
            login(request, user)
            messages.success(request, 'Registro de Cliente exitoso.')
            return redirect('/')
    else:
        form = RegistroForm()
    
    return render(request, 'autenticacion/registro.html', {
        'form': form, 
        'titulo_registro': 'Registro de Clientes'
    })

def registro_staff(request):
    if request.user.is_authenticated:
        return redirect('/') 

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            asignar_grupo_y_permisos(user, 'Staff', ['add_bike', 'change_bike'])
            login(request, user)
            messages.success(request, 'Registro de Staff exitoso.')
            return redirect('bicicletas:bike_list')
    else:
        form = RegistroForm()

    return render(request, 'autenticacion/registro.html', {
        'form': form, 
        'titulo_registro': 'Acceso para Personal'
    })