print ("ingrese la calidad del aire y sera clasificado")
iCA=int(input("ingrese el valor "))
if iCA<50:
    print ("bueno")
elif iCA>=50 and iCA<=100:
    print ("moderado")
else:
    print ("peligroso")