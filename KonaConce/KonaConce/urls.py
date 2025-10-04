from django.contrib import admin
from django.urls import path
from core import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('QuienesSomos/',views.QuienesSomos, name='quienes_somos'),
    path('FAQ/',views.FAQ, name='faq'),
    path('Galeria/',views.galeria, name='galeria_kona'),
    path('admin/', admin.site.urls),
    path("bicicletas/", include("bicicletas.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)