Nombre1 = input("Ingresa el primer nombre: ")

Nombre2 = input("Ingresa el segundo nombre: ")

Ordenados = sorted([Nombre1, Nombre2])

print("Los nombres ordenados alfabéticamente son:")
for nombre in Ordenados:
    print(nombre)