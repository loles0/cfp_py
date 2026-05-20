print ("ingrese un color como texto y se dira que estado representa")
color=(input("ingrese el color "))
if color=="rojo":
    print ("ocupado")
elif color=="verde":
    print ("disponible")
elif color=="azul":
    print ("en descanso")
else:
    print ("incorrecto")