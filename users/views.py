from django.shortcuts import render, HttpResponse, redirect

# wiews users
def index(request):
    respuesta="placeholder para que los usuarios creen un nuevo registro de usuario"
    return HttpResponse(respuesta)

def login(request):
    respuesta = "placeholder para que los usuarios inicien sesión"
    return HttpResponse(respuesta)

def root(request):
    respuesta="placeholder para luego mostrar toda la lista de usuarios"
    return HttpResponse(respuesta)

def new(request):
    return redirect("/users/register")
