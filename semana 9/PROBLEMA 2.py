#Calculadora que muestra el resultado de la multiplicacion de cualquier numero entero con los numeros del 0 al 12

A=int(input("Ingrese el numero: "))

for x in range(13) :
    resultado=A*x
    print(x," x ",A, " = ", resultado)
