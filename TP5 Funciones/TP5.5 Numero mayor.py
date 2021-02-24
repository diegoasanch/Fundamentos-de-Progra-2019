# Devolver el máximo entre dos números recibidos como parámetros.
def numeromayor(a,b):
    if a>b:
        mayor=a
    elif b>a:
        mayor=b
    else:
        mayor=False
    return mayor
# programa principal
print('Devolver el numero mayor de dos ingresados')
A=int(input('Ingrese un numero: '))
B=int(input('Ingrese otro numero: '))
maximo= numeromayor(A,B)
if maximo == False:
    print('Ambos numeros ingresados son iguales:',A)
else:
    print('El maximo de los numeros ingresados es:',maximo)