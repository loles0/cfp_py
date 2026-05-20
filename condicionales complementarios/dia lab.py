print ("ingrese un numero del 1 al 7 representando un dia de la semana (1:lunes, 7:domingo). sabrá so ese dia es laboral o no")
dia=int(input("ingrese el numero"))
if dia>=1 and dia<=5:
    print ("dia laborable")
elif dia>=6 and dia<=7:
    print ("fin de semana")
else:
    print ("numero incorrecto")