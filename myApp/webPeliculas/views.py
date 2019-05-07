from django.shortcuts import render

# Create your views here.
import copy

from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from webPeliculas.models import Actor,Pelicula,Puntuacion

def actoresPorNombre(request):
    a = list(Actor.objects.all().values())

    return JsonResponse(a, safe=False)

def actorPopular(request):
    a = Pelicula.objects.all().values()
    
    res = []
    for elemento in a:
        res.append(elemento)

    return JsonResponse(res, safe=False)

def mejorPelicula(request):
    lista = Pelicula.objects.all()
    pre_res = dict()

    for pelicula in lista:
        val = Puntuacion.objects.filter(fk_pelicula = pelicula.id)
        cont1 = 0
        cont2 = 0
        
        for puntuacion in val:
            cont1 += puntuacion.puntuacion
            cont2 += 1
        
        media = cont1/cont2

        pre_res[pelicula] = media

    iter_res = copy.deepcopy(pre_res)
    res = list()

    for i in range(0,2):
        max_key = None
        max_val = 0
        for element in iter_res.keys():
            media = iter_res[element]
            if max_val < media:
                max_key = element
                max_val = media
        res.append((max_key,max_val))
        del iter_res[max_key]
        
    
    return render(request, 'mejorPelicula.html', {'pelicula1':res[0], 'pelicula2':res[1]})