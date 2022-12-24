print("Datos del alumno:")
edad = int(input("Edad:"))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
puntaje = float(input("Puntaje obtenido en el examen: "))
if puntaje<=1000 and puntaje>750:
    print("Eres de la seccion A")
if puntaje<=750 and puntaje>350:
    print("Eres de la seecion B")
if puntaje<=350 and puntaje>0:
    print("Eres de la seccion C")