import tkinter as tk
from tkinter import ttk ##Paquete con mejoras visuales o estilos
from tkinter.messagebox import showinfo ##importa el paquete para enviar msj en ventanas
#Creamos una ventana

ventana = tk.Tk()

##Redimencionar la ventana

ventana.geometry("900x600")##es ancho x por alto

#Evitar redimencionar la ventana

ventana.resizable(0,0)

#Color de la ventana

ventana.configure(background="#1d2d44")

#Configurar el titulo de la ventana

ventana.title("Nuevo titulo")

boton1 = ttk.Button(ventana,text = "Boton1")
boton2 = ttk.Button(ventana,text = "Boton2")
boton3 = ttk.Button(ventana,text = "Boton3")

#Configurar el Grid
##Esto sirve para configurar el ancho de la fila y columna
ventana.columnconfigure(0,weight =1)
ventana.columnconfigure(1,weight =1)
ventana.columnconfigure(2,weight =1)

ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=1)
##Publicar usando grid Horizontal
#
boton1.grid(row=0,column=0)
boton2.grid(row=0,column=1)
boton3.grid(row=0,column=2)

#Publicar de manera vertical

boton1.grid(row=0,column=0)
boton2.grid(row=1,column=0)
boton3.grid(row=2,column=0)

#Publicar de manera diagonal

boton1.grid(row=0,column=0,sticky=tk.N)## Sticky hace que el boton se pocicione en en la posicion mas al norte(puede variar)
boton2.grid(row=1,column=1,sticky=tk.NW)
boton3.grid(row=2,column=2,sticky=tk.SE)


boton1.grid(row=0,column=0,padx=20,pady=20)##Mueve el boton 20 pixeles a la derecha y hacia abajo
boton2.grid(row=1,column=1,ipadx=20,ipady=20)#Agranda el boton
boton3.grid(row=2,column=2,sticky=tk.NS)#EStira el boton en todo el espacio que tiene de alto

ventana.mainloop()