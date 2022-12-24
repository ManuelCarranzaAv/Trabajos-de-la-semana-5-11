#A un trabajador se le paga por sus horas trabajadas y la tarifa por hora, si la cantidad de horas es mayor a 40 entonces el costo por 
# la hora extra será un 50% adicional a la tarifa por hora, calcular el salario total del trabajador.
tarifa = int(input("Ingrese la tarifa por horas: "))
horas = int(input("Ingrese las horas trabajadas: "))
salario = tarifa*horas

if salario>=320:
    print ("Tu salario es S/", salario,"te estan pagan bien")
else:
    print ("Tu salario es S/", salario, "te estan pagando poco")

