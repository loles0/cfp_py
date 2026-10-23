class personaje ():
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

p1 = personaje("maiton", 100)
p2 = personaje("sosa", 200)

print(p1.nombre, p1.vida)
print(p2.vida, p2.nombre)