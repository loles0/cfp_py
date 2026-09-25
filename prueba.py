import ttkbootstrap as ttk
ventana = ttk.Window(themename="cosmo")
ventana.title("formulario")
ventana.geometry("400x250")
ttk.Label(ventana, text="Nombre").pack(pady=10)
ttk.Entry(ventana).pack(pady=10)
ttk.Button(ventana, text="aceptar").pack(pady=10)
ventana.mainloop()