from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

def contacto_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            email = form.cleaned_data.get('email')
            asunto_usuario = form.cleaned_data.get('asunto', 'Consulta General') 
            mensaje = form.cleaned_data.get('mensaje')
            
            subject_mail = f'KonaConce: {asunto_usuario} (De: {nombre})'
            message_body = f"Has recibido un nuevo mensaje:\n\nNombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}"
            
            try:
                send_mail(
                    subject_mail,
                    message_body,
                    email, 
                    ['admin@konaconce.cl'], 
                    fail_silently=False,
                )
                messages.success(request, '¡Tu consulta ha sido enviada con éxito a Mailtrap!')
            except Exception as e:
                messages.error(request, f'Error al enviar: {e}')
                
            return redirect('formulario:vista_contacto')
    else:
        form = ContactForm()
    
    return render(request, 'formulario/formulario.html', {'form': form})