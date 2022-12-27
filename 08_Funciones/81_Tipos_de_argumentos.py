def desplegar(nombres):
    for nombre in nombres:
        print(nombre)


lista = ["Juan", "Carla", "Guillermo"]

desplegar(lista)
# Juan
# Carla
# Guillermo

desplegar("Eliseo ")
# E
# l
# i
# s
# e
# o


# pasar numero como argumento daria error

# pero si los pasamos como tuple funcionaria
desplegar((1, 2, 3))
