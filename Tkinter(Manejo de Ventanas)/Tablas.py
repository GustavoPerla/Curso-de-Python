import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.geometry("900x600")
ventana.title("Tablas")
ventana.resizable(0,0)
ventana.configure(background="#1d2d44")

#Configuramos el grid

ventana.columnconfigure(0,weight=1)

#Definir un estilo

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Treeview",background="black",
                 foreground="white",
                 fieldbackground="black",
                 rowheight=30
                 )
estilo.map("Treeview",background=[("selected","red")])

#Definimos las columnas

columnas= ("Id","Nombre","Edad")
tabla =ttk.Treeview(ventana, columns=columnas,show="headings")

#Cabeceros de la tabla

tabla.heading("Id",text="Id",anchor=tk.CENTER)
tabla.heading("Nombre",text="Nombre",anchor=tk.W)
tabla.heading("Edad",text="Edad",anchor=tk.E)

##Formato a las columnas
tabla.column("Id",width=80,anchor=tk.CENTER)##Ancho de la columna
tabla.column("Nombre",width=120,anchor=tk.W)##Ancho de la columna
tabla.column("Edad",width=120,anchor=tk.E)##Ancho de la columna

#Cargar datos a la tabla

datos = ((1,"Alexandra",25),(2,"Matias",32))
for x in datos:
    tabla.insert(parent="",index=tk.END,values=x)
tabla.grid(row=0,column=0,sticky= tk.NSEW)

#Agregamos un Scrollbar

scrollbar =ttk.Scrollbar(ventana,orient=tk.VERTICAL,command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0,column=1, sticky=tk.NS)

#Mostrar registros seleccionados

def mostrar_selecionados(event):
    element = tabla.item(tabla.selection()[0])
    persona = element["values"]
    showinfo(title="Persona seleccionada:",message=f"Persona: {persona[1]}")
tabla.bind("<<TreeviewSelect>>",mostrar_selecionados)

ventana.mainloop()