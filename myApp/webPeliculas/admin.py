from django.contrib import admin

# Register your models here.
from webPeliculas.models import Usuario,Categoria,Actor,Director,Pelicula,Puntacion

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Pelicula)
admin.site.register(Puntacion)