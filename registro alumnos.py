import tkinter as tk
from tkinter import ttk
ventana=tk.Tk()
ventana.title("registro de alumnos")
ventana.geometry("400x350")
notebook=ttk.Notebook(ventana)
notebook.pack()
pestaña1=ttk.Frame(notebook)
notebook.add(pestaña1,text="holas")
pestaña2=ttk.Frame(notebook)
notebook.add(pestaña2,text="holass")
ventana.mainloop()