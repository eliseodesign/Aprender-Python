def suma(a, b):
    return a + b  # con la palabra return regresamos este valor


resultado = suma(1, 2)
print(resultado)  # 3


# podemos tener valores por defecto para parametros

def multiplicacion(a=0, b=0) -> int:
    return a*b

# -> int  indica el tipo de dato que esperamos, pero no lo obliga ni marca eror


resultado2 = multiplicacion()
print(resultado2)  # 0
