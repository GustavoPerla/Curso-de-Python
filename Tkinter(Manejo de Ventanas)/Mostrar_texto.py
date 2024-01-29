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



etiqueta=ttk.Label(ventana,text="Saludos",background="#1d2d44",font=("Arial",78))
etiqueta.pack(pady= 20)

#Caja de texto

caja_texto = ttk.Entry(ventana, font=("Arial",15),background="#21a522") #Tipo de letra y tamaño
caja_texto.pack(pady=30)

##boton1 = ttk.Button(ventana, text="Enviar", command=saludar)## ATENCION el metodod saludar va sin parentesis
boton1 = ttk.Button(ventana, text="Enviar", command = lambda : etiqueta.configure(text= caja_texto.get()))
boton1.pack(pady=10)
ventana.mainloop()