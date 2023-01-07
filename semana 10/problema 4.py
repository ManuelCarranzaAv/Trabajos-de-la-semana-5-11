#Programar un codigo que de como resultado el factorial de un nummero entero.")
numero = int(input("Digite el numero que desea factorizar: "))
fact = 1
for i in range(1,numero+1):
    fact = fact * i
print("El resultado de factorizar",numero,"es: ",fact)