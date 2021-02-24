# Escribir la función comparar(a,b) que reciba como parámetros dos números
# enteros y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1
# si el primero es menor que el segundo. Ejemplo: comparar(4,2) devuelve 1, y
# comparar(2,4) devuelve -1.
def comparar(a,b):
    if a>b:
        v=1
    elif a==b:
        v=0
    else:
        v=-1
    return v
#programa principal
print('Comparador de numeros')
print()
A=int(input('Ingrese un numero: '))
B=int(input('Ingrese otro numero: '))
comparacion=comparar(A,B)
print(comparacion)