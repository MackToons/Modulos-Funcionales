import db.methods as dbm

# Programa principal que junta al resto de los modulos
def main():
    dbm.migraciones()

    print("main")

# Llama a la función main sólo si es ejecutado como script principal (`python main.py`)
if __name__ == "__main__":
    main()
