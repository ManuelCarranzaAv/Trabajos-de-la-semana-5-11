#Un fabricante de losetas se dispone a elaborar piezas,
#y cada loseta puede medir entre 0.3 y 0.4 metros de largo como mucho,
#Ingresar la cantidad de loseta y su medida respectiva, Por último el programa
#Deberá digitalizar la cantidad de piezas.

cantidad = 0
x = 1
n = int(input("Cuantas piezas cargara: \n"))
while x<=n:
    largo = float(input("Ingrese la medida la pieza: \n"))
    if largo>=0.3 and largo<=0.4:
        cantidad = cantidad + 1
    x = x + 1
print("La cantidad de piezas aptas son: ")
print(cantidad)