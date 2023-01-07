#Diseña un algoritmo en el que se ingrese 2 digitos para sumarlos
#y el programa los contabilice y los acumule usando el while.
#declaracion de variables
acum = 0 
cont = 0

rpt = "si"
while (rpt != "no"):
    num1 = int (input ("ingrese el primer numeros: "))
    num2 = int (input ("ingrese el segundo numeros: "))
    acum = acum + num1 + num2
    cont = cont + 2
    suma = num1 + num2
    print ("La suma es: ", suma)
    print("La acumulación de suma es de: " , acum)
    print("Contador de cuantos digitos ingresó: ", cont)

    rpt = str (input ("Desea realizar otra suma? si/no : "))