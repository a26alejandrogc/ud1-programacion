salario_bruto = float(input("Introduce el salario bruto: "))
irpf = float(input("Introduce el porcentaje de IRPF: "))
salario_neto = salario_bruto - (salario_bruto * irpf / 100)
print("El salario neto es:", salario_neto)  