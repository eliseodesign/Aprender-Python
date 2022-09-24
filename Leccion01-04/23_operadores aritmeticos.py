#OPERADORES MATEMATICOS
# OJO HAY DOS DE DIVISION
# /     ESTE DIVIDE TOTALMENTE
# //    ESTE DIVIDE SOLO ENTERO

a = float(input("a: "))
b = float(input("b: "))

suma = a+b
resta = a-b
multiplicación = a*b
divisionN = a/b
divisionE = a//b
modulo = a%b
exponente = a**b
print(f'______\n'
      f'Suma:           {suma} \n'
      f'Resta:{         resta} \n'
      f'Multiplicación: {multiplicación} \n'
      f'Division:       {divisionN} \n'
      f'Division (int): {divisionE} \n'
      f'Modulo:         {modulo} \n'
      f'Exponente:      {exponente}')



area = a*b
perimetro = (a + b)*2

print('\n_______________________________________________')
print(f'Si los datos proporcionados fueran alto y ancho \n en cm de un cuadrado tendria'
      f'\n'
      f'Area de {area} cm \n'
      f'Perimetro de {perimetro} cm ')