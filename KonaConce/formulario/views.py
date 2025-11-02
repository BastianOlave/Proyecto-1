from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contacto_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, '¡Tu consulta ha sido enviada con éxito!')
            return redirect('formulario:vista_contacto')
    else:
        form = ContactForm() 
    return render(request, 'formulario/formulario.html', {'form': form})