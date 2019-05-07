# P7 para AII por **alebarrod**

## Práctica 1 para AII - (acceso inteligente a la información)
Enunciado de la práctica del Departamento de Lenguajes y Sistemas (LSI) de la *Universidad de Sevilla* (http://www.lsi.us.es/docencia/pagina_asignatura.php?id=119&cur=2018):

"ACCESO INTELIGENTE A LA INFORMACIÓN PRÁCTICA DJANGO
Se desea construir una página web que permita recomendar a usuarios películas en función de las puntuaciones que han dado otros usuarios a las películas y los gustos de éstos.
En principio, se pide construir el modelo de datos y la interfaz de administración para los datos en Django que almacene la información siguiente:
a) Usuario: Nombre, apellidos, nombre de usuario, contraseña, e-mail, fecha de
nacimiento, categorías de películas que prefiere.
b) Puntuaciones asignadas por los usuarios a las películas. Las puntuaciones son entre 1 y 5.
c) Película: Título, año, actores principales, director, resumen, categoría/s (terror, comedia, etc..).
d) Actor: Nombre, apellidos, biografía, películas en las que actuó.
e) Director: Nombre, apellidos, biografía, películas que dirigió.
Se pide construir una web con un menú principal, en la parte superior de la ventana, que permita
las siguientes opciones:
a) Mostrar todos los actores (nombre, apellidos, biografía) ordenados por nombre.
b) Mostrar la películas (título y resumen) agrupadas por categoría.
c) Mostrar el actor (nombre y apellidos) que haya trabajado en más películas.
d) Mostrar los títulos de las dos películas mejor puntuadas (calculando la media)."

# Requisitos
- Tener instalado **Python 3** (el desarrollo se realizó bajo **Python 3.6**)
- Tener instalado **DJANGO 2.1.7**: https://docs.djangoproject.com/en/2.2/topics/install/

# Ejecución
Para ejecutar la aplicación unicamente debemos abrir una consola e ir al directorio en el que se encuentre `manage.py` y ejecutar `python manage.py runserver`.
La funcionalidad de la aplicación está explicada en el enunciado de la práctica.
