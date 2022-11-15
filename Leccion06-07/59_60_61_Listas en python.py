# una lista es un conjunto de elementos con un indice

nombres = ["Eliseo", "Kevin", "Gladis", "Genaro"]

#imprimir la lista
print(nombres) #['Eliseo', 'Kevin', 'Gladis', 'Genaro']
print(nombres[0]) #Eliseo


#########################
print("""#######################
"60"
"#######################
""")




#acceder a rangos de indices
print(nombres[1:3]) # ['Kevin', 'Gladis']

print(nombres[:3]) # ['Eliseo', 'Kevin', 'Gladis']


# Cambiar valor
nombres[0] = "Fran"
print(nombres)


#recorrer
for nombre in nombres:
    print((nombre))

#cantidad de elementos
print(len(nombres))


#agregar un elemento
nombres.append("Wendy")
print(nombres)


#incertar elemento en indice

nombres.insert(1, "Marcos")
print(nombres)

#remover
nombres.remove("Marcos")

#remover con pop
nombres.pop()
print(nombres)

#remover con indice
del nombres[0]
print(nombres)


#eliminar todos
nombres.clear()
print(nombres)

#o podemos eliminar la variable
del nombres
#print(nombres)
#imprimirla lista nos daira error porque ya no existe