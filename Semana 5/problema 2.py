# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#agregar la liberia math
#Conjunto de implementaciones que permiten codificar este lenguaje,
#-con el objeto de crear una interfaz independiente.
import math
#definir las variables
cateto1 = float(input("Introduce el cateto 1:"))
cateto2 = float(input("Introduce el cateto 2:"))

#Desarrollo de la operacion
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

#resultado de la operacion
print("La hipotenusa es",hipotenusa)

#expreciones logicas usadas en este codigo:

# #  "==,=" igual que    "**" potencia    "math.sqrt" raiz