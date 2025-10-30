'''
    Modulo de usuarios
'''

import utils

'''
    El sexto campo lo utilizamos para saltarnoslo,
    por que si esta en falso, es que se dio de baja
'''
def mostrarUsuarios(cursor):
    usuarios = utils.fetching(cursor)
    print("ID   |  Nombre   |  Fecha de nacimiento   |  Telefono   |  Correo\n")
    for usuario in usuarios:
        if usuario[6]:
            print(f"{usuario[0]}   |  {usuario[1]}, {usuario[2]}   |  {
                  usuario[3]}   |  {usuario[4]}   |  {usuario[5]}")
        else:
            continue

def ingresarUsuario(conn, apellido, nombre, fecha_nac, telefono, correo):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios(apellido, nombre, fecha_nac, telefono, correo)
        VALUES
            (?,?,?,?,?)''', (apellido, nombre, fecha_nac, telefono, correo))
    cursor.commit()
    cursor.close()

def modificarUsuario(conn, ID):
    cursor = conn.cursor()
    actualizar = utils.ingresarDatos()
    queries = []

    for pair in actualizar:
        query = f"UPDATE libros SET {pair[0]} = ? WHERE id = ?"
        queries.append((query, pair[1]))

    for pair in queries:
        cursor.execute(f"{pair[0]}", (pair[1], id))
    cursor.commit()
    cursor.close()

def darBaja(conn, id):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET estado = FALSE
        WHERE id = ?''', (id))
    cursor.commit()
    cursor.close()


def capturarDatos():
    pass
