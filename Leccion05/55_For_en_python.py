#ciclo for
cadena = "hola"

print(cadena.capitalize())#algo extra que descubre xd vuelve la primera letra mayuscula


for letra in cadena:
    print(letra)
else: #else es opcional y sucedera al final de la iteración
    print("fin")

print("-------------")

nombre = "holanda"

for n in nombre:
    if n == "a":
        print(f"se ha ecnontrado {n}")
        continue
    elif n:
        print(n)
else:
    print("fin")