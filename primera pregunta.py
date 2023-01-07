#Realiza un programa en el cual, si se ingresa un número 
#que esté entre el rango del 3 al 12, el programa volverá a pedir
#Que se ingrese un número, hasta que se detecte un número fuera del rango.


while True:
    num1 = int(input("Para seguir jugando un numero entre (3,12), para salir un numero fuera del rango: \n"))
    if num1>12 or num1<3:
        break

