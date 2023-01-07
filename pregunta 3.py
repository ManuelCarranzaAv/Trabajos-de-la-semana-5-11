#Crear un programa en el cual, Ingrese 10 valores, 
#y proceda a calcular su suma y promedio.

datos = int(input("Ingrese la cantidad de datos: \n"))
suma = 0
prom = 0
for i in range(1,datos+1):
    num = int(input("Escriba el numero: \n"))
    suma = suma + num
    prom = suma/datos
print("La suma total de los numeros es:", suma)
print("El promedio total de los numeros es:", prom)