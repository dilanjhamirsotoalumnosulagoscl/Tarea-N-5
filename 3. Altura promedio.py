alturas = []
num_alturas = 0

while True:
    altura = float(input("Ingresa la altura de la persona (en metros) o 0 para terminar: "))
    if altura == 0:
        break
    alturas.append(altura)
    num_alturas += 1

altura_promedio = sum(alturas) / num_alturas

print("La altura promedio de las personas es:", altura_promedio)
