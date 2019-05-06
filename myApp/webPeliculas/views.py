from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from webPeliculas.models import Actor,Pelicula,Categoria
from django.core import serializers


def actoresPorNombre(request):
    a = list(Actor.objects.order_by('nombre').values('nombre','apellidos','biografia'))

    return JsonResponse(a, safe=False)

def peliculasPorCategoria(request):
    a = list(Pelicula.objects.all())
    
    diccionario = dict()

    for element in a:
        diccionario[element.id] = list()
        for element2 in element.listaCategorias():
            valor = Categoria.objects.filter(id = element2.id).values()[0]['id']
            diccionario[element.id].append(valor)
            
    categorias = list(Categoria.objects.all())

    dicctionarioRes = dict()

    for cat in categorias:
        dicctionarioRes[cat] = list()

        for pelicula in diccionario.keys():
            if cat.id in diccionario[pelicula]:
                value = Pelicula.objects.filter(id = pelicula).values()[0]
                dicctionarioRes[cat].append(value)

    return render(request, 'peliculas.html', {'diccionario':dicctionarioRes})

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