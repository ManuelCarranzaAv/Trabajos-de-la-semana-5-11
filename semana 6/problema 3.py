#programa que pide una nota de un examen(del 0 al 20) por teclado y muestra
# la nota como "Sobresaliente", "Notable", "Bien", "Suficiente", "Suspendido". 
#estructura selctivas
#Multiples

a=float(input("ingrese la nota del examen: "))
if a >=0 and a <= 9:
    print("Suspenso")
elif a >= 10 and a<=11:
    print("Suficiente")
elif a >=12 and a <= 14:
	print("Bien")
elif a == 16 or a==17:
	print("Notable")
elif a >=18 or a <= 20:
	print("Sobresaliente")
else:
	print("La nota es incorrecta")

#elif: se usa cuando se quiera verficar varias condiciones  
# las declaraciones elif y else se realizan para una serie de comprobaciones.

#expreciones logicas
# #  ==,= igual que           >mayor que          <menor que          >=mayor o igual que          <=menor o igual que







