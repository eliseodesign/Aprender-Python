#Diccionario

diccionario = {
    "IDE": "Integrated Develoment Evironment",
    "OPP": "Objet Oriented Programing",
    "DBMS": "Database Management System"

}


print(diccionario)
print( len(diccionario) )
#UN DICCIOARIO NO POSEE INDICES POR LO QUE ACCEDEMOS CON LA LLAVE
print(diccionario["IDE"])
print(diccionario.get("IDE"))

#modificar
diccionario["IDE"]="ide"

print(diccionario)