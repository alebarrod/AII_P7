from django.shortcuts import render

# Create your views here.
import copy

from django.http import HttpResponse, HttpResponseNotFound,JsonResponse

from webPeliculas.models import Actor,Pelicula,Puntuacion,Categoria
from django.core import serializers


def actoresPorNombre(request):
    a = list(Actor.objects.order_by('nombre').values('nombre','apellidos','biografia'))

    return JsonResponse(a, safe=False)

def peliculasPorCategoria(request):
    pass
    
def actorPopular(request):
    a = list(Pelicula.objects.all())
    
    diccionario = dict()

    for element in a:
        for element2 in element.listaActores():
            #print(Actor.objects.filter(id = element2.id).values('id'))
            valor = Actor.objects.filter(id = element2.id).values('id')[0]['id']
            
            if valor in diccionario.keys():
                diccionario[valor] += 1
            else:
                diccionario[valor] = 1
            
    max_val = 0
    mas_populares = list()

    for element in diccionario.keys():
        valor = diccionario[element]
        if valor > max_val:
            max_val = valor
            mas_populares = list()
            mas_populares.append(element)
        elif valor == max_val:
            mas_populares.append(element)	

    res = ''
    for element in mas_populares:
        actor = Actor.objects.filter(id = element).values('nombre', 'apellidos')[0]
        res += actor['nombre'] + ', ' + actor['apellidos'] + ';'
    

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