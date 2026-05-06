print ("ingrese las coordenadas de los puntos A y B y se le devolvera la distancia entre ellos")
AX=float(input("ingrese la coordenada X de A: "))
AY=float(input("ingrese la coordenada Y de A: "))
BX=float(input("ingrese la coordenada X de B: "))
BY=float(input("ingrese la coordenada Y de B: "))
D= ((AX-BX)**2 + (AY-BY)**2)**0.5
print (D)