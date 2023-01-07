#Generar un programa, en el cual, nos asignen una pregunta, y de contestar mal, 
#Aparecerá respuesta errónea.

pregunta = input("¿Cual es la capital de Peru?: \n")
if pregunta == "lima":
    print("Respuesta valida")
else:
    print("Respuesta erronea")