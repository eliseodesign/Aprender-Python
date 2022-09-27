#SENTENCIA IF/ELSE
#SENTENCIA DE CONTROL

condicion = True

if condicion:
    print("condicion true")
else:
    print("condicion false")


numero = int(input("Ingrese numero entre 1 y 3:"))
texto = ""
if numero == 1:
    texto = "Uno"
elif numero == 2:
    texto = "Dos"
elif numero == 3:
    texto = "Tres"
else:
    texto = f"""Dije entre 1 y 3 >:(
¿Por que escribes {numero}?
"""

print(texto)