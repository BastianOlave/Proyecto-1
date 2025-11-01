from django.shortcuts import render
from .forms import ContactForm 

def contacto_view(request):
    form = ContactForm() 
    return render(request, 'formulario/formulario.html', {'form': form})