from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from webPeliculas.models import Actor

def actoresPorNombre(request):
    a = list(Actor.objects.all().values())

    return JsonResponse(a, safe=False)