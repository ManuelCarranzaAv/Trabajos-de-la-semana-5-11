print("Digite los catetos y hipotenusa de un triangulo rectangulo para calcular el perimetro")
cateto1 = float(input("Coloque el primer cateto: "))
if cateto1<0:
    print("DATO INCORRECTO")
    cateto1 = float(input("Coloque el primer cateto: "))
cateto2 = float(input("Coloque el segundo cateto: "))
if cateto2<0:
    print("DATO INCORRECTO")
    cateto2 = float(input("Coloque el segundo cateto: "))
hipotenusa = float(input("Coloque la hipotenusa: "))
if hipotenusa<cateto1 or hipotenusa<cateto2:
    print("DATO INCORRECTO")
    hipotenusa = float(input("Coloque la hipotenusa: "))
PERIMETRO = cateto1 + cateto2 + hipotenusa
print("El perimetro del triangulo es: ",PERIMETRO)