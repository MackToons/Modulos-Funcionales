import tkinter as tk

def menuCirculacion():
    root = tk.Tk()
    root.minsize(width=640, height=480)

    WIDTH_ = 12
    HEIGHT_ = 2

    #Top row con mensaje de bienvenida
    bienvenida = tk.Label(root, text="Sistema virtual de biblioteca - Modulo de Circulacion")
    bienvenida.grid(column=0, row=0)

    #Definicion de botones del menu principal
    botonBusquedaCirculacion = tk.Button(root, text="Busqueda")
    botonPrestarLibro = tk.Button(root, text="Prestar un libro")
    botonDevolverLibro = tk.Button(root, text="Devolver un libro")
    BotonVolver = tk.Button(root, text="Volver")

    #Dibujamos en la pantalla principal los botones
    botonBusquedaCirculacion.grid(column=0, row=1)
    botonPrestarLibro.grid(column=0, row=2)
    botonDevolverLibro.grid(column=0, row=3)
    BotonVolver.grid(column=0, row=4)

    #Configuracion del tamaño de los botones
    botonBusquedaCirculacion.config(width=WIDTH_, height=HEIGHT_)
    botonPrestarLibro.config(width=WIDTH_, height=HEIGHT_)
    botonDevolverLibro.config(width=WIDTH_, height=HEIGHT_)
    BotonVolver.config(width=WIDTH_, height=HEIGHT_)

    root.mainloop()
