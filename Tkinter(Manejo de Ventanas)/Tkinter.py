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

#Creamos una etiqueta

etiqueta=ttk.Label(ventana,text="Saludos",background="#1d2d44")

#Cambiar el texto usando el metodo configure

etiqueta.configure(text="Hola mundo",background="#1d2d45")

#Cambiar el texto con la ayuda de la llaves (es como un diccionario)

etiqueta["text"]= "Pepe"

#Mostramos el componente de etiqueta

etiqueta.pack(pady=200) ##en esas cordenadas


##Creacion de botones

saludar = lambda : showinfo(title="Mensaje privado",message="Juan mecanico")## esto muestra una ventana con un msj

#Caja de texto

caja_texto = ttk.Entry(ventana, font=("Arial",15),background="#21a522") #Tipo de letra y tamaño
caja_texto.pack(pady=30)

##boton1 = ttk.Button(ventana, text="Enviar", command=saludar)## ATENCION el metodod saludar va sin parentesis
boton1 = ttk.Button(ventana, text="Enviar", command=lambda : showinfo(title="Mensaje privado",message="Juan mecanico")) ##Tambien se puede hacer asi
boton1.pack(pady=10)


#Hacemos visible la ventana

ventana.mainloop()