#crear un algoritmo donde el alumno digitará su nota, donde sabrá si aprobo o desaprobó")
nota = int(input("Digite su nota: \n"))
if nota>20 or nota<0:
    print("NOTA NO VALIDA")
    nota = int(input("Digite su nota: "))
if 20>=nota>10:
    print("APROBADO")
elif 0<=nota<=10:
    print("DESAPROBADO")

