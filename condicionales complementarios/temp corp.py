print ("ingrese la temperatura corporal en C° y sera clasificado")
temp=float(input("ingrese el valor "))
if temp<36:
    print ("hipotermia")
elif temp>=36 and temp<=37.5:
    print ("normal")
else:
    print ("fiebre")