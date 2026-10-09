import ttkbootstrap as ttk
from ttkbootstrap import Messagebox
ventana=ttk.Window()
ventana.title("aprender")
ventana.geometry("450x250")
def ventanax():
    ventanaxx=ttk.Toplevel(ventana)
    ventanaxx.title("mas info")
    ventanaxx.geometry("350x150")
    esu_label=ttk.Label(ventanaxx, text="milton schwindt").pack()
    
    ventanaxx.grab_set()
bton=ttk.Button(ventana, text="abrir", command=ventanax).pack()
ventana.mainloop()


