import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora de compra")
ventana.geometry("600x500")

tk.Label(ventana, text="Nombre").pack()
nombre_entrada = tk.Entry(ventana)
nombre_entrada.pack()

tk.Label(ventana, text="Precio del producto").pack()
precio_entrada = tk.Entry(ventana)
precio_entrada.pack()

tk.Label(ventana, text="Cantidad").pack()
cantidad_entrada = tk.Entry(ventana)
cantidad_entrada.pack()

var_envio = tk.BooleanVar()
var_garantia = tk.BooleanVar()
var_instalacion = tk.BooleanVar()
tk.Checkbutton(ventana, text="Envío ($5.000)", variable=var_envio).pack()
tk.Checkbutton(ventana, text="Garantía ($10.000)", variable=var_garantia).pack()
tk.Checkbutton(ventana, text="Instalación ($15.000)", variable=var_instalacion).pack()

resultado_etiqueta = tk.Label(ventana, text="", justify="left")
resultado_etiqueta.pack(pady=10)


def calcu():
    cliente = nombre_entrada.get().strip()
    try:
        precio = float(precio_entrada.get())
        cantidad = int(cantidad_entrada.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos en precio y cantidad")
        return

    if not cliente or precio < 0 or cantidad <= 0:
        messagebox.showerror("Error", "Complete el nombre y use valores positivos")
        return

    subtotal = precio * cantidad
    servicios = 0
    if var_envio.get():
        servicios += 5000
    if var_garantia.get():
        servicios += 10000
    if var_instalacion.get():
        servicios += 15000

    descuento = subtotal * 0.10 if subtotal > 200000 else 0
    total = subtotal + servicios - descuento
    resultado_etiqueta.config(
        text=(
            f"Cliente: {cliente}\n"
            f"Subtotal: ${subtotal:,.2f}\n"
            f"Servicios: ${servicios:,.2f}\n"
            f"Descuento: -${descuento:,.2f}\n"
            f"Total: ${total:,.2f}"
        )
    )


tk.Button(ventana, text="Calcular", command=calcu).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.destroy).pack()
ventana.mainloop()