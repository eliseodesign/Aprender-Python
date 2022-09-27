mes = int(input("introduce el mes del año (1-12):"))
estacion = None


if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    estacion = f"numero {mes} no corresponde a un mes "

print(f'''
Para el mes {mes}
La estación es {estacion}''')


print("------------------------------------")
nota = int(input("introduce la calificación:"))
valor = ""

if 9 <= nota <= 10:
    valor = "A"
elif 8 <= nota < 9:
    valor = "B"
elif 7 <= nota < 8:
    valor = "C"
elif 6 <= nota < 7:
    valor = "D"
elif 0 <= nota < 6:
    valor = "F"
else:
    valor = "invalido"


print(f"el resultado fue {valor}")

