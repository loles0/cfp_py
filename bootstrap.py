import ttkbootstrap as ttk
ventana=ttk.Window(themename="flatly")
ventana.title("sexo")
ventana.geometry("400x450")
def saludo():
    broski.config(text=f"bro")
etiqeta=ttk.Label(
    ventana,
    text="hola bro"
).pack()
boton=ttk.Button(
    ventana,
    text="hermano",
    command=saludo
)
boton.pack()
broski=ttk.Label(ventana, text="")
broski.pack()
ventana.mainloop()