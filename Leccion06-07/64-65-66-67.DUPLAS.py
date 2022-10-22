# una tupla es similar a una lista solo que no la podemos modificar
# tipo inmutalbe
# tuple

frutas = ("naranja", "platano", "manzana")

#funciones similares a lista
print(frutas)

c = len(frutas)
print(c)

print(frutas[2])


#Crear una lista a partir de una tupla con solo los valores menores a 5

tupla = (13,4,5,3,1,12,8,2)
lista = []
for t in tupla:
    if(t < 5):
        lista.append(t)

print(lista)