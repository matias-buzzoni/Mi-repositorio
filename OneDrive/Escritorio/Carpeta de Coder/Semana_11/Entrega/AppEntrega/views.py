from django.shortcuts import render

# Create your views here.

def Inicio(request):
    return render(request,"inicio.html")

def Cliente(request):
    return render(request,"cliente.html")

def Vendedor(request):
    return render(request,"vendedor.html")

def Mayorista(request):
    return render(request,"mayorista.html") 

def cursoForm(request):
    if request.method == "POST": #Post para enviar
        curso = Curso(request.POST[nombre["nombre"], request.POST["camada"]) #trae del template los datos de los input
        curso.save()
        return render(request,"inicio.html")              
return render(request,"cursoForm.html")



