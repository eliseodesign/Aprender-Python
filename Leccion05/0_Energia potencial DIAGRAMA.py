#ejercicio hecho en diagrama llevdo a codigo
# NECECITAMOS
# 3 varaibles (2 de ingreso y la de salida) y una constante, la gravedad
# tomar en cuenta que m != 0, h != 0
# Ep=mgh
def peticion():
    global m, g, h # definir estas variables como globales
    m = int(input("Introduce la masa:"))
    g = 9.81
    print(f'gravedad: {g}')
    h = int(input("Introduce la altura:"))

def operacion():
    global ep
    ep = m*g*h
    return ep

def go():
    if m <= 0 or h <= 0:
        print(f'''ERROR -
    los datos ingresados son incorrectos no puede ingresar numeros negativos)
    peticion
    ''')
        peticion()
        go()
    elif m >= 0 or h >= 0:
        print(operacion())

peticion()
go()
