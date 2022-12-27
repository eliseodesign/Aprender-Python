#funcion que detecta si es palindromo

def palindromo():
    palabra = input("escribe una palbara")
    palabraNew = palabra [::-1]
    if palabraNew == palabra:
        print("es palidromo")
    else:
        print("no es palindromo")


palindromo()