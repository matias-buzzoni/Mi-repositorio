import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola soy Matias")

def segunda_vista(request):
    return HttpResponse("<br><br> Ya entendi esto? es muy simple? jaja ")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es día: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombrees(request, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)



def probandoTemplate(self):
    miHtml= open ("C:/Users/Usuario/OneDrive/Escritorio/Carpeta de Coder/Django/MiProyecto1/Templates/Soyyo/index.html")
    plantilla = Template (miHtml.read()) #se carga en memoria el index
    miHtml.close() # se cierra el archivo
    miConTexto = Context() #aca no hay parametros pero igual se crea esto
    documento = plantilla.render(miConTexto) #se renderiza la planilla con el documento 
    return HttpResponse(documento)