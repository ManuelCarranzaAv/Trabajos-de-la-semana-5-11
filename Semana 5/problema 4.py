# Dadas dos variables numéricas A y B, que el usuario debe teclear, 
# se pide realizar un algoritmo que intercambie los valores de ambas variables 
# y muestre cuanto valen al final las dos variables.

#definir variables
a = int(input("Introduce el valor de la variable A:"))
b = int(input("Introduce el valor de la variable B:"))
#cambio de variables
aux = a
a = b
b = aux
#expresion de la operacion
print("Nuevo valor de A:", a)
print("Nuevo valor de B:", b)

#problema de estrucutura de asignacion,
#Asignarle un dato a una variable consiste en reemplazar el valor anterior o inicial de la variable con un valor nuevo. 
#Una vez que se asigna un nuevo valor, el valor anterior es eliminado de la memoria