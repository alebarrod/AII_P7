from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from webPeliculas.models import Actor,Pelicula,Categoria
from django.core import serializers

def actoresPorNombre(request):
    a = list(Actor.objects.order_by('nombre').values('nombre','apellidos','biografia'))

    return render(request, 'actoresNombre.html', {'lista':a})

def peliculasPorCategoria(request):
    a = list(Pelicula.objects.all().values())
    b = Categoria.objects.all().values()
    c = list()
    for element in b:
        c.append(Pelicula.objects.filter(categorias=element['id']).values('titulo','resumen'))

    return JsonResponse(str(c), safe=False)