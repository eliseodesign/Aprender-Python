#recorrer diccionarios
diccionario = {
    "IDE": "Integrated Develoment Evironment",
    "OPP": "Objet Oriented Programing",
    "DBMS": "Database Management System"
}

#acceder a la llave
for termino in diccionario:
    print(termino)

#acceder a llave y termino
for termino, valor in diccionario.items():
    print(termino, valor)


#acceder los terminos
for termino in diccionario.keys():
    print(termino)

# valor
for valor in diccionario.values():
    print(valor)

# comprobar si existe
print("IDE" in diccionario)

#agregar
diccionario["PK"] ="Primary Key"
print(diccionario)


#remover
diccionario.pop("PK")
print(diccionario)

#fuciona el clear() y el del