# Una funcion recursiva es una que se llama asi misma

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


resultado = factorial(5)


print(resultado)
