#codigo para mostrar si es un numero divisible por 3 o 5.")
numero = input("Digite su numero: ")
suma = 0
ultima = int(numero)%10
div3 = suma%3
if div3 == 0:
     print("El numero "+str(numero)+" es divisible por 3")
else:
     print("El numero "+str(numero)+" no es divisible por 3")
div5 = ultima%5
if ultima == 5 or ultima == 0:
     print("El numero "+str(numero)+" es divisible por 5")
else:
     print("El numero "+str(numero)+" no es divisible por 5")