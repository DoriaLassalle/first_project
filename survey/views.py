from django.shortcuts import render, HttpResponse

# wiews survey

def index(request):
    respuesta="placeholder para luego mostrar todas las encuestas creadas"
    return HttpResponse(respuesta)

def  new(request):
    respuesta = "placeholder para que los usuarios agreguen una nueva encuesta"
    return HttpResponse(respuesta)