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
cumpleaños_var=tk.Radiobutton(ventana, text="cumpleaños", variable=evento_var, value="cumpleaños")
casamiento_var=tk.Radiobutton(ventana, text="casamiento", variable=evento_var, value="casamiento")
empresarial_var=tk.Radiobutton(ventana, text="empresarial", variable=evento_var, value="empresarial")
servicios_var=tk.BooleanVar()
sonido_var=tk.Checkbutton(ventana, text="Dj y sonido ($40.000)", variable=servicios_var, value="sonido")
sonido_var.pack()
comida_var=tk.Checkbutton(ventana, text="Cathering/comida ($80.000)", variable=servicios_var, value="comida")
comida_var.pack()
foto_var=tk.Checkbutton(ventana, text="Fotografia ($30.000)", variable=servicios_var, value="foto")
foto_var.pack()

servicio=int()
if sonido_var.get():
    servicio += 40000
if comida_var.get():
    servicio += 80000
if foto_var.get():
    servicio += 30000
    subtotal=invitados_entrada.get()*2000

def calc ():
    try:

    nombre=nombre_entrada.get()

    invitados=invitados_entrada.get()

    if invitados > 100:

        descuento=int(subtotal*0.15)

        total=float(subtotal-descuento)

    except ValueError:
        messagebox.showerror("error", "ingrese valores correctos")
    return
    