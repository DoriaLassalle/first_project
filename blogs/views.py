from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

def index(request):
    respuesta="placeholder para luego mostrar una lista de todos los blogs"
    return HttpResponse(respuesta)

def root(request):
    return redirect("/blogs")

def  new(request):
    respuesta = "placeholder pra mostrar un nuevo formulario para crear un nuevo blog"
    return HttpResponse(respuesta)

def create(request):
    return redirect("/")

def show(request, number):
    respuesta= f"placeholder para mostrar el blog numero: {number}"
    return HttpResponse(respuesta)

def edit(request, number):
    respuesta = f"placeholder para editar el blog: {number}"
    return HttpResponse(respuesta)

def destroy(request, number):
    return redirect("/blogs")

def bonus(request):
    resp=({"nombre":"Doria",
            "apellido":"Lassalle",
            "alterego":"Dorio"})
    return JsonResponse(resp)

  