from django.urls import path
from . import views

urlpatterns = [
    path("", views.holaDjango, name="holaDjango"),
    path("pepe", views.pepe, name="Hola Pepe"),
    path('<str:nombre>', views.holaTu, name='holaTu'),
    path('indice', views.indice, name='indice')
    ]