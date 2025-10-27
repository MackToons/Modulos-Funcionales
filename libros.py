'''
    Modulo de libros
'''

from utilidades import fetching

def mostrarLibros(cursor):
    libros = fetching(cursor)
    print("ID   |  ISBN   |  TITULO   |  AUTOR   |  STOCK   |  AÑO DE PUBLICACION   |  DISPONIBLE\n")
    for libro in libros:
        print(f"{libro[0]}   |  {libro[1]}   |  {libro[2]}   |  {libro[3]}   |  {
              libro[4]}   |  {libro[5]}   |  {"Si" if libro[6] else "No"} \n")

def ingresarLibro():
    pass

def modificarLibro():
    pass

def eliminarLibro():
    pass

def realizarPrestamo():
    pass
