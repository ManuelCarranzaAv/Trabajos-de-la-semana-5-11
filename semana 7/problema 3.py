#El alumno procedera a poner sus notas de P1, P2, PC, EF, el programa arrojara si aprobó o desaprobó")
numero1 = float(input("Coloque la nota de P1: "))
if numero1<0 or numero1>20:
    print("NOTA NO VALIDA")
    numero1 = float(input("Coloque la nota de P1: "))
numero2 = float(input("Coloque la nota de P2: "))
if numero2<0 or numero2>20:
    print("NOTA NO VALIDA")
    numero2 = float(input("Coloque la nota de P2: "))
numero3 = float(input("Coloque la nota de PC: "))
if numero3<0 or numero3>20:
    print("NOTA NO VALIDA")
    numero3 = float(input("Coloque la nota de PC: "))
numero4 = float(input("Coloque la nota de EF: "))
if numero4<0 or numero4>20:
    print("NOTA NO VALIDA")
    numero4 = float(input("Coloque la nota de EF: "))

PROMEDIO = (numero1+numero2+numero3+numero4)/4
print("Su promedio final es: ",PROMEDIO )