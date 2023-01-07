#En una empresa se quiere empezar a programar el monto total de un servicio")
numero1 = float(input("Coloque la cantidad del producto: "))
if numero1<0:
    print("Cantidad no valida")
    numero1 = float(input("Coloque la cantidad del producto: "))
numero2 = int(input("Coloque el valor unitario del producto: "))
if numero2<0:
    print("Monto no valido")
    numero2 = int(input("Coloque el valor unitario del producto: "))
#operacion
TOTAL=(numero1*numero2)+18/100*(numero1*numero2)
print("El monto total del servicio es: ",TOTAL)