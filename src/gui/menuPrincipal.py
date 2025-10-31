import tkinter as tk
import utilidades as util
import menuCirculacion as mc
import menuUsuarios as mu
import menuLibros as ml

root = tk.Tk()
root.minsize(width=640, height=480)

WIDTH_ = 22
HEIGHT_ = 5

#Marco para las opciones
opcionesMarco = tk.Frame(root, width=300, height=600, bg="lightblue", relief=tk.RAISED, bd=2)
opcionesMarco.grid(column=0, row=1, sticky="nsew")

#Marco para mensaje de bienvenida
bienvenidaMarco = tk.Frame(root, width=400, height=800, bg="lightblue", relief=tk.RAISED, bd=2)
bienvenidaMarco.grid(column=0, row=0, sticky="nsew")

#Marco para el cuerpo principal
cuerpoPrincipalMarco = tk.Frame(root, width=800, height=400, bg="gray", relief=tk.RAISED, bd=2)
cuerpoPrincipalMarco.grid(column=1, row=1, sticky="nsew")

#Top row con mensaje de bienvenida
bienvenida = tk.Label(bienvenidaMarco, text="Sistema virtual de bibliotecas")
bienvenida.grid(column=0, row=0)

#Definicion de botones del menu principal
botonSocios = tk.Button(opcionesMarco, text="Socios", command=mu.menuUsuarios)
botonLibros = tk.Button(opcionesMarco, text="Libros", command=ml.menuLibros)
botonCirculacion = tk.Button(opcionesMarco, text="Circulación", command=mc.menuCirculacion)
botonAcercaDe = tk.Button(opcionesMarco, text="Acerca de")
BotonSalir = tk.Button(opcionesMarco, text="Salir", command=lambda: util.salirAplicacion(root))

#Dibujamos en la pantalla principal los botones
botonSocios.grid(column=0, row=1)
botonLibros.grid(column=0, row=2)
botonCirculacion.grid(column=0, row=3)
botonAcercaDe.grid(column=0, row=4)
BotonSalir.grid(column=0, row=5)

#Configuracion del tamaño de los botones
botonSocios.config(width=WIDTH_, height=HEIGHT_)
botonCirculacion.config(width=WIDTH_, height=HEIGHT_)
botonLibros.config(width=WIDTH_, height=HEIGHT_)
botonAcercaDe.config(width=WIDTH_, height=HEIGHT_)
BotonSalir.config(width=WIDTH_, height=HEIGHT_)

root.mainloop()
