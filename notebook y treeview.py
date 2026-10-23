import json
from pathlib import Path

import ttkbootstrap as ttk
from ttkbootstrap import Messagebox


ARCHIVO_JSON = Path(__file__).with_name("Videojuegos.json")

ventana = ttk.Window(themename="solar")
ventana.title("Mi colección de videojuegos")
ventana.geometry("1050x700")
ventana.minsize(800, 560)

estilo = ttk.Style()
estilo.configure("Treeview", rowheight=34, font=("Segoe UI", 10))
estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

pestania = ttk.Notebook(ventana)
pestania.pack(fill="both", expand=True, padx=28, pady=24)

pagina_juegos = ttk.Frame(pestania, padding=24)
pagina_agregar = ttk.Frame(pestania, padding=24)
pestania.add(pagina_juegos, text="  Mi colección  ")
pestania.add(pagina_agregar, text="  Agregar juego  ")

ttk.Label(
    pagina_juegos,
    text="Mi colección de videojuegos",
    font=("Segoe UI", 22, "bold"),
).pack(anchor="w")
ttk.Label(
    pagina_juegos,
    text="Tus juegos, plataformas y precios en un solo lugar.",
    bootstyle="secondary",
).pack(anchor="w", pady=(4, 18))

columnas = ("Videojuegos", "Plataforma", "Precio")
trviu = ttk.Treeview(
    pagina_juegos,
    columns=columnas,
    show="headings",
    height=12,
)
trviu.heading("Videojuegos", text="VIDEOJUEGO")
trviu.heading("Plataforma", text="PLATAFORMA")
trviu.heading("Precio", text="PRECIO")
trviu.column("Videojuegos", width=420, minwidth=200, anchor="w")
trviu.column("Plataforma", width=260, minwidth=160, anchor="w")
trviu.column("Precio", width=160, minwidth=100, anchor="center")
trviu.tag_configure("par", background="#f0f4f8")
trviu.tag_configure("impar", background="#ffffff")

barra = ttk.Scrollbar(pagina_juegos, orient="vertical", command=trviu.yview)
trviu.configure(yscrollcommand=barra.set)
trviu.pack(side="left", fill="both", expand=True)
barra.pack(side="right", fill="y")

ttk.Label(
    pagina_agregar,
    text="Agregar un videojuego",
    font=("Segoe UI", 22, "bold"),
).pack(anchor="w")
ttk.Label(
    pagina_agregar,
    text="Completa los datos para añadirlo a tu colección.",
    bootstyle="secondary",
).pack(anchor="w", pady=(4, 18))

formulario = ttk.Frame(pagina_agregar, padding=24, bootstyle="light")
formulario.pack(fill="x", padx=70, pady=12)

ttk.Label(formulario, text="Nombre del videojuego").pack(anchor="w")
nom = ttk.Entry(formulario)
nom.pack(fill="x", pady=(5, 16))

ttk.Label(formulario, text="Plataforma").pack(anchor="w")
PLat = ttk.Entry(formulario)
PLat.pack(fill="x", pady=(5, 16))

ttk.Label(formulario, text="Precio").pack(anchor="w")
precio = ttk.Entry(formulario)
precio.pack(fill="x", pady=(5, 22))


def guardar_videojuegos():
    lista = []

    for iid in trviu.get_children():
        videojuego, plataforma, precio_juego = trviu.item(iid, "values")
        lista.append(
            {
                "videojuego": videojuego,
                "plataforma": plataforma,
                "precio": precio_juego,
            }
        )

    with ARCHIVO_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, ensure_ascii=False, indent=4)


def cargar_videojuegos():
    if not ARCHIVO_JSON.exists():
        return

    with ARCHIVO_JSON.open("r", encoding="utf-8") as archivo:
        lista = json.load(archivo)

    for juego in lista:
        cantidad = len(trviu.get_children())
        trviu.insert(
            "",
            "end",
            values=(juego["videojuego"], juego["plataforma"], juego["precio"]),
            tags=("par" if cantidad % 2 == 0 else "impar",),
        )


def agregor():
    videojuego = nom.get().strip()
    platforma = PLat.get().strip()
    preciosss = precio.get().strip()

    if not videojuego or not platforma or not preciosss:
        Messagebox.show_error("No deje casillas en blanco.", "Error")
        return

    cantidad = len(trviu.get_children())
    trviu.insert(
        "",
        "end",
        values=(videojuego, platforma, preciosss),
        tags=("par" if cantidad % 2 == 0 else "impar",),
    )
    guardar_videojuegos()

    nom.delete(0, "end")
    PLat.delete(0, "end")
    precio.delete(0, "end")
    nom.focus_set()
    pestania.select(pagina_juegos)


ttk.Button(
    formulario,
    text="Agregar a mi colección",
    command=agregor,
    bootstyle="primary",
).pack(fill="x")

cargar_videojuegos()
ventana.mainloop()
