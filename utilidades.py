'''
    Funciones que sirven para varios modulos.
'''
from time import sleep
import os

def fetching(cursor):
    fetched = cursor.fetchall()
    return fetched

def mostrarPrestamos():
    # que lindo inner join voy a tener que hacer
    pass

def menu():
    print("Bienvenido a la biblioteca Virtal\n")
    print("1.Cargar usuario\n 2.Cargar Libro\n 3.Prestamos\n 4.Modificar\n 5.Busqueda\n 6.Salir\n")
    opc = input("Opcion: ")
    
    match opc:
        case 1:
            menu()
        case 2:
            menu()
        case 3:
            menu()
        case 4:
            menuModificar()
            menu()
        case 5:
            menu()
        case _:
            print("Opcion invalida! Seleccione otra.")
            menu()
    pass


def menuModificar():
    print("1.Modificar usuario\n 2. Modificar libro\n 3.Salir\n")
    opc = input("Opcion: ")
    match opc:
        case 1:
            menuModificar()
        case 2:
            menuModificar()
        case 3:
            print("Volviedo al menu principal...")
            sleep(2)
            menu()
        case _:
            print("Opcion invalida! Seleccione otra.")
            sleep(2)
            limpiarTerminal()
            menuModificar()

def limpiarTerminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def ingresarDatos():
    datos = []