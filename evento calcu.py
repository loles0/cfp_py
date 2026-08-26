import tkinter as tk
ventana=tk.Tk()
from tkinter import messagebox
from tkinter import ttk
ventana.title("reserva de salón")
ventana.geometry("400x600")

nombre_etiqueta=tk.Label(ventana, text="ingrese su nombre").pack()
nombre_entrada=tk.Entry(ventana)
nombre_entrada.pack()
invitados_etiqueta=tk.Label(ventana, text="ingrese la cantidad de invitados").pack()
invitados_entrada=tk.Entry(ventana)
invitados_entrada.pack()
evento_var=tk.StringVar()
cumpleaños_var=tk.Radiobutton(ventana, 
                              text="cumpleaños", 
                              variable=evento_var, 
                              value="cumpleaños")
casamiento_var=tk.Radiobutton(ventana, 
                              text="casamiento", 
                              variable=evento_var, 
                              value="casamiento")
empresarial_var=tk.Radiobutton(ventana, 
                               text="empresarial", 
                               variable=evento_var, 
                               value="empresarial")
sonido_var=tk.BooleanVar()
comida_var=tk.BooleanVar()
foto_var=tk.BooleanVar()
sonido_checkbutton=tk.Checkbutton(ventana, 
                          text="Dj y sonido ($40.000)", 
                          variable=sonido_var)
sonido_checkbutton.pack()
comida_checkbutton=tk.Checkbutton(ventana, 
                          text="Cathering/comida ($80.000)", 
                          variable=comida_var)
comida_checkbutton.pack()
foto_checkbutton=tk.Checkbutton(ventana,
                         text="Fotografia ($30.000)", 
                         variable=foto_var)
foto_checkbutton.pack()

def calc():
    try:
        nombre = nombre_entrada.get()
        invitados = int(invitados_entrada.get())
        subtotal = invitados * 2000          # ← aquí el cambio importante
        servicio = 0

        if sonido_var.get():
            servicio += 40000
        if comida_var.get():
            servicio += 80000
        if foto_var.get():
            servicio += 30000

        if invitados >= 100:
            descuento = int(subtotal * 0.15)
            total = subtotal - descuento
            totals= total+servicio
            resultado_etiqueta.config(
                text=f"{nombre} por haber invitado a 100 o más personas\n"
                     f"se le ha hecho un descuento del 15%\n"
                     f"(-${descuento}) y el precio final queda en ${totals}"
            )
        else:
            descuento = 0
            total = subtotal
            totals=total+servicio
            resultado_etiqueta.config(text=f"{nombre} el total es de ${totals}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese valores correctos")


boton_C=tk.Button(
    ventana,
    text="calcular",
    command=calc
).pack()
resultado_etiqueta=tk.Label(
    ventana,
    text=""
)
resultado_etiqueta.pack()
boton_S=tk.Button(
    ventana,
    text="salir",
    command=ventana.destroy
).pack()
ventana.mainloop()