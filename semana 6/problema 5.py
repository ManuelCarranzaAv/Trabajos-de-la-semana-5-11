#A un trabajador se le paga por sus horas trabajadas y la tarifa por hora.
tarifa = int(input("Ingrese la tarifa por horas: "))
horas = int(input("Ingrese las horas trabajadas: "))
salario = tarifa*horas

if salario>=320:
    print ("Tu salario es S/", salario,"te estan pagando bien")
else:
    print ("Tu salario es S/", salario, "te estan pagando poco")

