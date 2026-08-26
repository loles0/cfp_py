import tkinter as tk
ventana=tk.Tk()
from tkinter import ttk
ventana.title("nuevo estudiante")
ventana.geometry("600x400")


nombre_etiqueta=tk.Label(
    ventana,
    text="ingrese su nombre y apellido"
)
nombre_etiqueta.pack()
nombre_entrada=tk.Entry(ventana)
nombre_entrada.pack()

edad_etiqueta=tk.Label(
    ventana,
    text="ingrese su edad"
)
edad_etiqueta.pack()
edad_entrada=tk.Entry(ventana)
edad_entrada.pack()
sexo_etiqueta=tk.Label(
    ventana,
    text="seleccione su sexo"
)
#variable que guarda la opcion elegida
sexo_var=tk.StringVar()
#botones de opcion
tk.Radiobutton(
    ventana,
    text="masculino",
    variable=sexo_var,
    value="masculino"
).pack()
tk.Radiobutton(
    ventana,
    text="femenino",
    variable=sexo_var,
    value="femenino"
).pack()
tk.Radiobutton(
    ventana,
    text="otro",
    variable=sexo_var,
    value="otro"
).pack()

curso_etiqueta=tk.Label(
    ventana,
    text="seleccione su curso"
).pack()
#desplegable de cursos
cursos = ["1° año", "2° año", "3° año"]
curso_combo = ttk.Combobox(
    ventana,
    values=cursos,
    state="readonly"
)
curso_combo.pack()

def mues ():
    nombre=nombre_entrada.get()
    edad=edad_entrada.get()
    sexo=sexo_var.get()
    curso=curso_combo.get()
    datos_etiqueta.config(text=f"{nombre}, de {edad} años de edad, sexo {sexo} del curso {curso},ha sido registrado en el sistema")

datos_etiqueta=tk.Label(
    ventana,
    text=""
)
datos_etiqueta.pack()
boton=tk.Button(
    ventana,
    text="registrarse",
    command=mues
)
boton.pack()
boton_S=tk.Button(
    ventana,
    text="salir",
    command=ventana.destroy
).pack()
ventana.mainloop()