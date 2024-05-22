sueldos = []
num_empleados_500_900 = 0
num_empleados_mas_900 = 0
total_sueldos = 0

while True:
    sueldo = float(input("Ingresa el sueldo del empleado (en pesos) o -1 para terminar: "))
    if sueldo == -1:
        break
    if sueldo >= 500000 and sueldo <= 900000:
        num_empleados_500_900 += 1
    elif sueldo > 900000:
        num_empleados_mas_900 += 1
    sueldos.append(sueldo)
    total_sueldos += sueldo

print("Cantidad de empleados que cobran entre $500.000 y $900.000:", num_empleados_500_900)
print("Cantidad de empleados que cobran más de $900.000:", num_empleados_mas_900)
print("El total gastado en sueldos es de:", total_sueldos)