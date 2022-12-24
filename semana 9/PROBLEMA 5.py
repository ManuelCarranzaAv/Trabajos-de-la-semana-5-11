#Mencionar todas las vocales de  cualquier palabra que deseo escribir

A=input("Ingrese la palabra: ")

for cadena in A :
    if cadena in "aeiouAEIOUÁÉÍÓÚáéíóú" :
        print(cadena)