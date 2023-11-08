
from django.urls import path,include
from AppEntrega.models import *
from AppEntrega.views import *
from AppEntrega import views



urlpatterns = [
    path("inicio/",Inicio, name ="home"), #primer view
    path("clientes/",views.Cliente, name ="cliente"),
    path("vendedor/",views.Vendedor, name="vendedor"),
    path ("mayorista/",views.Mayorista,name="mayorista"),


    #url de form
    path("cursoForm/",cursoForm,name="cursoForm"),
    

]
