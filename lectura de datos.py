import ttkbootstrap as ttk
def mostrar_nombre():
    nombre=entrada.get()
    resultado.config(text="nombre: "+ nombre)

ventana=ttk.Window()
ventana.title("Lectura de datos")
ventana.geometry("450x250")

ttk.Label(ventana, text="Ingrese su nombre:").pack(pady=10)

entrada=ttk.Entry(ventana)
entrada.pack(pady=10)

ttk.Button(ventana, text="MOSTRAR", command=mostrar_nombre).pack(pady=10)

resultado=ttk.Label(ventana, text="")
resultado.pack(pady=10)
ventana.mainloop()