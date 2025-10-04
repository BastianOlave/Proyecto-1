from django.urls import path
from . import views

app_name = "bicicletas"

urlpatterns = [
    path("", views.bike_list, name="bike_list"),
    path("<int:pk>/", views.bike_detail, name="bike_detail"),
]

