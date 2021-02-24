#Leer un número natural N. Calcular e imprimir los primeros N números naturales
#impares.
print('Ingrese un numero N y vea en pantalla los primeros N naturales impares')
print()
N=int(input('Ingrese un numero natural: '))
if N>0:
    impares=0
    cont=1
    while cont<=N:
        if impares%2==1:
            print(impares)
            cont=cont+1
        impares=impares+1
    print('Esos son los primeros',N,'naturales impares')
else:
    print('No ingreso un numero natural')