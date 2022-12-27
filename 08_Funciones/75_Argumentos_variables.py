# cuando no conocemos la cantidad de elemento que recibira una funcion se ura *


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres("Eliseo", "Kevin", "Wendy", "Genaro")
# Eliseo
# Kevin
# Wendy
# Genaro


# ARGUMENTOS VARIABLES LLAVE - VALOR

# Recibir diccionario
def listaTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave}: {valor}")


listaTerminos(IDE="Integrated Develoment Eviroment")
