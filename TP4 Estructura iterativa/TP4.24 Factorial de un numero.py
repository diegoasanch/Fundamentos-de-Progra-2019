#El factorial de un número entero N mayor que cero se define como el producto
#de todos los enteros X tales que 0 < X <= N. Desarrollar un programa para calcular el factorial de un
#número dado. Deberán rechazarse las entradas inválidas (menores que 0).
print('Factorial de un numero N! ingrese un numero>0')
print()
N=int(input('Ingrese un numero: '))
print()
if N>0:
    factorial=N
    cont=N-1
    while cont>0:
        factorial=factorial*cont
        cont=cont-1
    print(N,'! Es',factorial)
else:
    print('No ingreso un numero natural')