# Calcular el perímetro y área de un rectángulo dada su base y su altura.
#Ingresar la pregunta con el sigueinte codigo

print("halle el area y el perimetro de un rectangulo con los siguientes datos: ")

#definir las variables
base=float(input("Introduce la base:"))
altura=float(input("Introduce la altura:"))

#desarrollo de la operacion
perimetro = 2 * (base + altura)
area = base * altura

#resultado de la operacion
print("El perimetro es", perimetro, "y el area es", area)

#expreciones logicas usadas en este codigo:

# #  "==,=" igual que    "*" multiplicacion  "+" suma