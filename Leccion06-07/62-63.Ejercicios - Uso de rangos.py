#Sintaxis range
# range(inicio, fin, incremento)
# fin -> obligatorio


# Imprimir numero divisible entre 3

for n in range(10):
    if n % 3 !=0:
        continue
    else:
        print(n)

print("- - - - - - -")

#Crear rango de numeros de 2 a 6

for n in range(2,6):
    print(n)


print("- - - - - - -")


#Crear un rango de 1 - 10 con incremento de 2 en 2

for n in range(2,10,2):
    print(n)