from django.contrib import admin
from AppEntrega import models
from AppEntrega.models import Cliente, Vendedor, Mayorista

# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.Vendedor)
admin.site.register(models.Mayorista)