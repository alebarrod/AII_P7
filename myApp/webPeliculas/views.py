from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from webPeliculas.models import Actor

def actoresPorNombre(request):
    a = list(Actor.objects.order_by('nombre').values('nombre','apellidos','biografia'))

    return JsonResponse(a, safe=False)