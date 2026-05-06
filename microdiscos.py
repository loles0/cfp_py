MD=1.44
print ("ingrese el tamaño de la copia de seguridad en GB y sabrá cuantos discos se necesitan para guardarla")
GB=int(input("tamaño de la copia de seguridad en GB: "))
MB=GB*1024
TMD: int=MB/MD
print ("se necesitan ", TMD, "discos para guardar la copia de seguridad")