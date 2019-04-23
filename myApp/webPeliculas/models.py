from django.db import models

from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=30)
    contrasenya = models.CharField(max_length=30)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    usuarios = models.ManyToManyField(Usuario)

class Actor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    biografia = models.CharField(max_length=100)

class Director(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    biografia = models.CharField(max_length=100)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=30)
    anyo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=30)

    fk_director = models.ManyToManyField(Director)
    actores = models.ManyToManyField(Actor)
    categorias = models.ManyToManyField(Categoria)

class Puntacion(models.Model):
    puntacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    fk_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    