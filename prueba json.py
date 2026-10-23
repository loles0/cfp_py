import ttkbootstrap as ttk
from ttkbootstrap import Messagebox
import json
from pathlib import Path
alumno = {
    "id": 1,
    "nombre": "Ana",
    "Apellido": "Gomez",
    "curso": "3ª"
}
texto_json=json.dumps(alumno, indent=4, ensure_ascii=False)
print(texto_json)
with open("alumno.json", "w", encoding="utf-8") as archivo:
    json.dump(alumno, archivo, indent=4, ensure_ascii=False)
print("datos guardados correctamente.")
with open ("alumno.json","r", encoding="utf-8") as archivo:
    datos_recuperados = json.load(archivo)
    for registro in datos_recuperados:
        print(registro)
archivo = Path("alumno.json")
if archivo.exists():
    print ("el archivo existe.")
else:
    print ("el archivo todavia no existe.")