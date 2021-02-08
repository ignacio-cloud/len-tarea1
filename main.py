from io import open
"""
manejo de archivos en python es importante ya que con ello se
puede leer un archivo escribir en el mismo o crear un archivo
que no existe.
la funcion open(..) es la utiliza en python para este proposito.

"r" read: leer un archivo si el archivo no existe salta un error.
"a" add: agregar texto al final del archivo si el archivo no existe lo crea.
"w" write: sobre escribe un archivo si el archivo no existe lo crea.
"x" crear: crea un archivo si este no existe.

"""

archivo = open("textos.txt", "w")
