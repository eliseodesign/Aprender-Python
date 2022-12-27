#OPERADORES LOGICOS
#AND OR NOT


a = True
b = False

# AND -> a and b
if a and b:
    print("true de and")
else:
    print("false de and")

#OR -> a or b
if a or b:
    print("true de or")
else:
    print("false de or")

#NOT -> not a
if not a:
    print("true de not")
else:
    print("false de not")



print("----------------------------------------")
print("QUE NUMERO ES MAYOR")
uno = int(input("numero 1:"))
dos = int(input("numero 2:"))

if not uno == dos:
    if uno > dos:
        print(f'{uno} es mayor que {dos}')
    elif dos > uno:
        print(f'{dos} es mayor que {uno}')
else:
    print(f'Los numeros {uno} y {dos} son iguales')