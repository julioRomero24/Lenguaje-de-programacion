from django.shortcuts import render,HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"proyectoFinal/inicio.html")
    #return render(request,"proyectoFinal/inicio.html")

def documentacion(request):
    return render(request,"proyectoFinal/documentacion.html")

'''def layout(request):
    return render(request,"proyectoFinal/layout.html")
'''