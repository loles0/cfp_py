PRC = 3
PRI = -1
PRB = 0
print ("ingrese el numero de respuestas correctas, incorrectas y en blanco del alumno y se le devolvera en forma de promedio")
RC =int(input("respuestas correctas: "))
RI =int(input("respuestas incorrectas: "))
RB =int(input("respuestas en blanco: "))
PF = (RC * PRC) + (RI * PRI) + (RB * PRB)
print ("el promedio del alumno es: ", PF)