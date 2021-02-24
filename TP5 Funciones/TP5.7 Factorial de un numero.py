# Dado un número entero, calcular su factorial. Ejemplo: fact(4) = 4*3*2*1 = 24.
#funcion factorial
def fact(n):
    if n==1:
        factorial = 1
    else:
        factorial = n * fact(n-1)
    return factorial

# programa principal
print('Calculador del factorial de un numero')
print()
A=int(input('Ingrese un numero: '))
resultado= fact(A)
print('El factorial de',A,'es =',resultado)