#Leer diez números enteros e imprimir el mayor.
print('leer 10 numeros enteros e imprimir el mayor')
print()
cont=1
n=int(input('Ingrese un numero entero: '))
mayor=0
while cont<10:
    cont=cont+1
    if n>mayor:
        mayor=n
    n=int(input('Ingrese un numero entero: '))
print('El mayor numero ingresado fue',mayor)
    