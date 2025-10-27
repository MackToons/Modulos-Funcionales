'''
    Modulo de usuarios
'''

from utilidades import fetching

'''
    El sexto campo lo utilizamos para saltarnoslo,
    por que si esta en falso, es que se dio de baja
'''
def mostrarUsuarios(cursor):
    usuarios = fetching(cursor)
    print("ID   |  Nombre   |  Fecha de nacimiento   |  Telefono   |  Correo\n")
    for usuario in usuarios:
        if usuario[6]:
            print(f"{usuario[0]}   |  {usuario[1]}, {usuario[2]}   |  {
                  usuario[3]}   |  {usuario[4]}   |  {usuario[5]}")
        else:
            continue

def ingresarUsuario():
    # no quiero validar datos wawawwaaz
    pass

def modificarUsuario():
    pass

def darBaja():
    pass
