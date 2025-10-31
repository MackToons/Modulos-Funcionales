import tkinter as tk

def menuLibros():
    root = tk.Tk()
    root.minsize(width=640, height=480)

    WIDTH_ = 12
    HEIGHT_ = 2

    #Top row con mensaje de bienvenida
    bienvenida = tk.Label(root, text="Sistema virtual de biblioteca - Modulo de libros")
    bienvenida.grid(column=0, row=0)

    #Definicion de botones del menu principal
    botonBusquedaLibro = tk.Button(root, text="Buscar")
    botonAgregarLibro = tk.Button(root, text="Nuevo Libro")
    botonDeshabilitarLibro = tk.Button(root, text="Deshabilitar")
    botonModificarLibro = tk.Button(root, text="Modificar datos")
    BotonVolver = tk.Button(root, text="Volver")

    #Dibujamos en la pantalla principal los botones
    botonBusquedaLibro.grid(column=0, row=1)
    botonAgregarLibro.grid(column=0, row=2)
    botonDeshabilitarLibro.grid(column=0, row=3)
    botonModificarLibro.grid(column=0, row=4)
    BotonVolver.grid(column=0, row=5)

    #Configuracion del tamaño de los botones
    botonAgregarLibro.config(width=WIDTH_, height=HEIGHT_)
    botonDeshabilitarLibro.config(width=WIDTH_, height=HEIGHT_)
    botonModificarLibro.config(width=WIDTH_, height=HEIGHT_)
    botonBusquedaLibro.config(width=WIDTH_, height=HEIGHT_)
    BotonVolver.config(width=WIDTH_, height=HEIGHT_)

    root.mainloop()
