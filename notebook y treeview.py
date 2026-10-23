import ttkbootstrap as ttk
ventana=ttk.Window(themename="solar")
ventana.title("Videojuegos")
ventana.geometry("1500x850")
pestania=ttk.Notebook(ventana)
columnas= ("Videojuegos", "Plataforma", "Precio")

Videojuegos=ttk.Frame(ventana, padding=20)
trviu=ttk.Treeview(Videojuegos, columns=columnas, show="headings")
agregarrrr=ttk.Frame(ventana, padding=20)
pestania.pack(padx=80, pady=80, fill="both", expand=True)
pestania.add(Videojuegos, text="Videojuegos")
pestania.add(agregarrrr, text="Agregar nuevo")


ttk.Label(Videojuegos, text="hola jaja").pack()


trviu.heading("Videojuegos", text="Videojuegos")
trviu.heading("Plataforma", text="Plataforma")
trviu.heading("Precio", text="Precio")
trviu.column("Videojuegos", width=180)
trviu.column("Plataforma", width=180)
trviu.column("Precio", width=180)
trviu.pack(fill="both", expand=True, padx=180, pady=180)
nom=ttk.Entry(agregarrrr)
ttk.Label(agregarrrr,text="Agregar nuevo juego").pack()
ttk.Label(agregarrrr,text="Nombre:").pack()
nom.pack(padx=10, pady=10)
ttk.Label(agregarrrr,text="Plataforma:").pack()
PLat=ttk.Entry(agregarrrr)
PLat.pack()











ventana.mainloop()