import tkinter as tk
from tkinter import ttk
ventana=tk.Tk()
ventana.title("contactos")
ventana.geometry("400x250")


def apert ():
    ventana_num= tk.Toplevel(ventana)
    ventana_num.title("agregar contacto")
    ventana_num.geometry("400x250")
    nombre_etiqueta=ttk.Label(
    ventana_num,
    text="nombre"
    ).pack()
    nombre_entry=ttk.Entry(ventana_num) 
    nombre_entry.pack()
    telefono_label=ttk.Label(
        ventana_num,
        text="telèfono"
    ).pack()
    telefono_entry=ttk.Entry(ventana_num)
    telefono_entry.pack()
    correo_label=ttk.Label(
        ventana_num,
        text="correo electronico"
    ).pack()
    correo_entry=ttk.Entry(ventana_num)
    correo_entry.pack()
    def contactis():
        nombre=nombre_entry.get()
        telefono=telefono_entry.get()
        correo=correo_entry.get()
        contacto=f"{nombre} // {telefono} // {correo}"
        contactos.insert(tk.END, contacto)
    def botonardo():
        contactis()
        ventana_num.destroy()
    agregar_bot=ttk.Button(
        ventana_num,
        text="ingresar",
        command=botonardo
    )
    agregar_bot.pack()

def borrar_contacto():
    seleccionado=contactos.curselection()
    if seleccionado:
        contactos.delete(seleccionado[0])


cont=ttk.Label(
    ventana,
    text="contactos"
).pack()
contactos=tk.Listbox(ventana, width=120, height=40)
contactos.pack(padx=20, pady=20)


apret_bot=ttk.Button(
    ventana,
    text="agregar contacto",
    command=apert
)
borrar_bot=tk.Button(
    ventana,
    text="borrar contacto",
    command=borrar_contacto
)
apret_bot.pack()
borrar_bot.pack()
boton=tk.Button(
    ventana,
    text="salir",
    command=ventana.destroy
)
boton.pack()



ventana.mainloop()