from django.contrib import admin
from django.urls import path
from django.views import saludo, segunda_vista,diaDeHoy, miNombrees, probandoTemplate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segundavista/', segunda_vista),
    path('fecha/', diaDeHoy),
    path('nombre/<nombre>/', miNombrees),
    path ("template/",probandoTemplate)
]

