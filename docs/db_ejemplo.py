'''
    Modulo de ejemplo que muestra como crear la base de datos y las tablas.

    Deberíamos separar sus funcionalidades en pequeñas funciones a llamar
    o preparar de antemano las queries que necesitamos y llamarlas desde
    los otros modulos.
'''
from utilidades import fetching
import sqlite3

#Conectamos a la DB, y si no existe la crea
connection = sqlite3.connect('biblioteca.db')

#Creamos un cursor objeto para ejecutar sentencias SQL
cursor = connection.cursor()

#Creamos las tablas necesarias: usuarios, libros, prestamos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INT PRIMARY KEY,
        apellido varchar(32) NOT NULL,
        nombre varchar(32) NOT NULL,
        fecha_nac DATE NOT NULL,
        telefono INT,
        correo varchar(64) NOT NULL,
        estado BOOL DEFAULT TRUE
    );
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros(
        id INT PRIMARY KEY,
        isbn varchar(32) NOT NULL,
        titulo varchar(32) NOT NULL,
        autor varchar(32) NOT NULL,
        stock INT NOT NULL CHECK(stock >= 0),
        fecha_pub INT NOT NULL,
        estado BOOL DEFAULT TRUE
    );
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS prestamos(
        id INT PRIMARY KEY,
        id_usuario INT NOT NULL,
        id_libro INT NOT NULL,
        fecha_venc DATETIME NOT NULL,
        fecha_pres DATETIME NOT NULL,
        CONSTRAINT fk_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
        CONSTRAINT fk_libro
        FOREIGN KEY (id_libro) REFERENCES libros(id)
    );
    ''')

#Hacemos un commit para guardar lo que hemos hecho
connection.commit()

#Ingresamos valores para probar las tablas: usuarios y libros
cursor.execute('''
    INSERT INTO usuarios(id, apellido, nombre, fecha_nac, telefono, correo)
        VALUES
            (1, 'Urquiza', 'Jose', '1985-10-01', 3874918012, 'jose.urquiza@mail.com'),
            (2, 'Veron', 'Mario', '1989-03-06', 3875981774, 'mario.veron@mail.com'),
            (3, 'Herrera', 'Marco', '1995-11-18', 3874019284, 'marco.herrera@mail.com');
    ''')

cursor.execute('''
    INSERT INTO libros (id, isbn, titulo, autor, stock, fecha_pub)
        VALUES
            (1, '9782306123315', 'Nosferatu', 'Bram Stoker', 3, 1987),
            (2, '9784345201419', 'El Alquimista', 'Paulo Coelho', 5, 1988),
            (3, '9785307299518', 'Harry Potter y la piedra filosofal', 'J. K. Rowling', 1, 1997);
    ''')

#Guardamos los cambios
connection.commit()

#Mostramos los usuarios ingresados
#print("Usuarios ingresados: \n")
#cursor.execute("SELECT * FROM usuarios")
#usuarios = cursor.fetchall()

#for usuario in usuarios:
#    print(f"ID: {usuario[0]}, Nombre: {usuario[1]} {usuario[2]}, Fecha de nacimiento: {usuario[3]}, Telefono: {usuario[4]}, Correo: {usuario[5]}\n")

#Mostramos los libros ingresador
#print("Libros ingresados: \n")
#cursor.execute("SELECT * FROM libros")
#libros = cursor.fetchall()

#for libro in libros:
#    print(f"ID: {libro[0]}, ISBN: {libro[1]}, Titulo: {libro[2]}, Autor: {libro[3]}, Publicacion: {libro[5]}, Disponible: {libro[6]}\n")

cursor.execute("SELECT * FROM usuarios;")
tabla = fetching(cursor)

for x in tabla:
    for i in range(len(x)):
        print(f"{x[i]} ")
    print("\n")
