from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.QuienesSomos, name='quienes_somos'),
    path('faq/', views.FAQ, name='faq'),
    path('galeria/', views.galeria, name='galeria_kona'),
]
