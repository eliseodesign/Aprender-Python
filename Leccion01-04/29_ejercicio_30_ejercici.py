#Determinar si un numero es par o impar
print("DETERMINAR NUMERO PAR O IMPAR")
a = int(input("Ingrese un numero entero:"))

if a % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")


print("_______________________________")

print("DETERMINAR SI ES MAYOR DE EDAD")
edad = int(input("Introduce tu edad:"))

if edad >= 18:
    print("Asi es, eres mayor de edad")
else:
    print("No no no, eres menor")
