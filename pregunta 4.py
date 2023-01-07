#Introduce una contraseña, en la cual si no es la contraseña correcta,
#Intruso, introduce la contraseña correcta, y si es la correcta
#Que resalte en la pantalla Contraseña correcta.

contraseña = input("Digite su contraseña: \n")
if contraseña == "1234":
    print("Contraseña correcta")
else:
    print("¡INTRUSOOOO!")
