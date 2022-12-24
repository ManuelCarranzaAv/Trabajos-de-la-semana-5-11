print("El alumno procedera a poner sus notas de IO, PC, EM, EB, el programa arrojara si aprobó o desaprobó")
numero1 = float(input("Coloque la nota de IO...... "))
if numero1<0 or numero1>20:
    print("NOTA NO VALIDA")
    numero1 = float(input("Coloque la nota de IO...... "))
numero2 = float(input("Coloque la nota de PC...... "))
if numero2<0 or numero2>20:
    print("NOTA NO VALIDA")
    numero2 = float(input("Coloque la nota de PC...... "))
numero3 = float(input("Coloque la nota de EM...... "))
if numero3<0 or numero3>20:
    print("NOTA NO VALIDA")
    numero3 = float(input("Coloque la nota de EM...... "))
numero4 = float(input("Coloque la nota de EB...... "))
if numero4<0 or numero4>20:
    print("NOTA NO VALIDA")
    numero4 = float(input("Coloque la nota de EB...... "))

PROMEDIO = (numero1+numero2+numero3+numero4)/4
print("Su promedio final es: ",PROMEDIO )