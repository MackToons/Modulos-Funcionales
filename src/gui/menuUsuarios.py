import tkinter as tk

def menuUsuarios():
    root = tk.Tk()
    root.minsize(width=640, height=480)

    WIDTH_ = 12
    HEIGHT_ = 2

    #Top row con mensaje de bienvenida
    bienvenida = tk.Label(root, text="Sistema virtual de biblioteca - Modulo de socios")
    bienvenida.grid(column=0, row=0)

    #Definicion de botones del menu principal
    botonBusquedaUsuario = tk.Button(root, text="Buscar")
    botonAgregarUsuario = tk.Button(root, text="Nuevo socio")
    botonBajaUsuario = tk.Button(root, text="Dar de baja")
    botonAltaUsuario = tk.Button(root, text="Dar de alta")
    botonModificarUsuario = tk.Button(root, text="Modificar datos")
    BotonVolver = tk.Button(root, text="Volver")

    #Dibujamos en la pantalla principal los botones
    botonBusquedaUsuario.grid(column=0, row=1)
    botonAgregarUsuario.grid(column=0, row=2)
    botonBajaUsuario.grid(column=0, row=3)
    botonAltaUsuario.grid(column=0, row=4)
    botonModificarUsuario.grid(column=0, row=5)
    BotonVolver.grid(column=0, row=6)

    #Configuracion del tamaño de los botones
    botonBusquedaUsuario.config(width=WIDTH_, height=HEIGHT_)
    botonAgregarUsuario.config(width=WIDTH_, height=HEIGHT_)
    botonBajaUsuario.config(width=WIDTH_, height=HEIGHT_)
    botonAltaUsuario.config(width=WIDTH_, height=HEIGHT_)
    botonModificarUsuario.config(width=WIDTH_, height=HEIGHT_)
    BotonVolver.config(width=WIDTH_, height=HEIGHT_)

    root.mainloop()
