print ("nivel de bateria")
bat=int(input("ingrese el nivel de bateria "))
if bat==100:
    print ("cargado completamente")
elif bat<99 and bat>20:
    print ("bateria adecuada")
elif bat<20 and bat>0:
    print ("bateria baja")
else:
    print ("incorrecto")