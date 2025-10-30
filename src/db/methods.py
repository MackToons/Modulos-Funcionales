'''
    Archivo principal con las funciones de la DB.
'''
import sqlite3

# Conexión a la base de datos. No exportar.
_conn: sqlite3.Connection

def connect() -> sqlite3.Connection:
    global _conn
    _conn = sqlite3.connect('biblioteca.db', timeout=10)
    return _conn

def migraciones() -> None:
    # Crear todas las tablas en esta función
    print('MIGRACIONES')
