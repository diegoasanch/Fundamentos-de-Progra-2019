#Leer un número natural N. Calcular e imprimir los números naturales pares menores que N.
print('Imprime los naturales pares menores que un numero natural cualquiera')
print()
n=int(input('Ingrese un numero natural: '))
if n>0:
    inicial=n
    n=n-1
    while n>=0:
        if n%2==0:
            print(n)
        n=n-1
    print('Esos son todos los naturales pares menores que',inicial)
else:
    print('No ingreso un numero natural')        