from django.urls import path
from .views import registro_cliente, registro_staff
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'autenticacion'

urlpatterns = [
    path('registro/cliente/', registro_cliente, name='registro_cliente'),
    path('registro/staff/', registro_staff, name='registro_staff'),
    
    path('login/', LoginView.as_view(
        template_name='autenticacion/login.html',
        redirect_authenticated_user=True 
    ), name='login'),
    
    path('logout/', LogoutView.as_view(), name='logout'),
]