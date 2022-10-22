# un set no mantiene el orden
# no permite duplicados
# si es posibl agregar

planetas = {"Marte", "Venus", "Jupiter"}

print(planetas) # orden aleatorio

#funciones parecidas
print(len(planetas))

#preguntar si contiene elemento
print('Marte' in planetas)

planetas.add("Tierra")
print(planetas)

#no se puede agregar dupplicados
planetas.add("Tierra")


#eliminar elemento
planetas.remove("Tierra") # si no existe mandaria error
print(planetas)

planetas.discard("Tierra") #no da eror si no existe

#limpiar el set
planetas.clear()

del planetas