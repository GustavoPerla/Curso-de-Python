import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

ventana =tk.Tk()

ventana.geometry("600x400")
ventana.title("Sistema de login")
ventana.resizable(0,0)
ventana.configure(background="#1d2d44")
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)

#creamos un estilo

estilo = ttk.Style()
estilo.theme_use("clam")##Por defaul maneja colores claros Clam maneja lso oscuros
estilo.configure(ventana,background="black",
                 foreground="white",
                 fieldbackground="black"
                 )
estilo.configure("TFrame",background="black")

##Agregamos un frame ##es como una ventana dentro de la ventana

frame = ttk.Frame(ventana)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(0,weight=3)

etiqueta = ttk.Label(frame,text="Login",font=("Arial",20))
etiqueta.grid(row= 0, column=0, columnspan=2)


etiqueta_usuario = ttk.Label(frame,text="Usuario:")
etiqueta_usuario.grid(row=1, column=0,sticky=tk.W,padx=5,pady=20)

text_box = ttk.Entry(frame)
text_box.grid(row=1,column=1,sticky=tk.E,padx=5,pady=5)

etiqueta_password = ttk.Label(frame,text="Password:")
etiqueta_password.grid(row=2, column=0,sticky=tk.W,padx=5,pady=20)

text_box1 = ttk.Entry(frame,show="*")
text_box1.grid(row=2,column=1,sticky=tk.E,padx=5,pady=5)

boton = ttk.Button(frame,text="Enviar")
boton.grid(row=3,column=0,columnspan=2)

frame.grid(row=0,column=0)

def validar(event):
    usuario = text_box.get()
    password = text_box1.get()
    if usuario == "root" and password == "admin":
        showinfo(title="Login",message="Usuario correcto!")
    else:
        showerror(title="Login", message="Usuario incorrecto!")

boton.bind("<Return>",validar)
boton.bind("<Button-1>",validar)

ventana.mainloop()
