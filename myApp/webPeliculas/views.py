from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from webPeliculas.models import Actor,Pelicula

def actoresPorNombre(request):
    a = list(Actor.objects.all().values())

    return JsonResponse(a, safe=False)

def actorPopular(request):
    a = Pelicula.objects.all().values()
    
    res = []
    for elemento in a:
        res.append(elemento)

    return JsonResponse(res, safe=False)