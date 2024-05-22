preguntas=int(input("Ingresa la cantidar de preguntas: "))
correctas=int(input("Ingresa la cantidad de preguntas correctas: "))

porcentaje=(correctas/preguntas)*100

if porcentaje >=95:
    print("Tu nivel es el maximo")
else:
    if porcentaje >=70:
        print("Tu nivel es el medio")
    else:
        if porcentaje >=40:
            print("Tu nivel es el regular")
        else:
            if porcentaje <40:
                print("Estas fuera del nivel")