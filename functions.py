def ingresar():
    inp = input()
    return inp

def fetching(cursor):
    fetched = cursor.fetchall()
    return fetched

#El sexto campo lo utilizamos para saltarnoslo, por que si esta en falso, es que se dio de baja
def mostrarUsuarios(cursor):
    usuarios = fetching(cursor)
    print("ID   |  Nombre   |  Fecha de nacimiento   |  Telefono   |  Correo\n")
    for usuario in usuarios:
        if usuario[6]:
            print(f"{usuario[0]}   |  {usuario[1]}, {usuario[2]}   |  {usuario[3]}   |  {usuario[4]}   |  {usuario[5]}")
        else:
            continue

def mostrarLibros(cursor):
    libros = fetching(cursor)
    print("ID   |  ISBN   |  TITULO   |  AUTOR   |  STOCK   |  AÑO DE PUBLICACION   |  DISPONIBLE\n")
    for libro in libros:
        print(f"{libro[0]}   |  {libro[1]}   |  {libro[2]}   |  {libro[3]}   |  {libro[4]}   |  {libro[5]}   |  {"Si" if libro[6] else "No"} \n")
    
def mostrarPrestamos():
    #que lindo inner join voy a tener que hacer 

def ingresarUsuario():
    #no quiero validar datos wawawwaaz
    
def ingresarLibro():

def modificarUsuario():

def modificarLibro():
    
def eliminarLibro():
    
def realizarPrestamo():
    
def menu():
    
def darBaja():