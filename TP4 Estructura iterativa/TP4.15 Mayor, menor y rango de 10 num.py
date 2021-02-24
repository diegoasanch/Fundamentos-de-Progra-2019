#Leer diez números e imprimir el mayor, el menor y el rango del conjunto
#(El rango de un conjunto se calcula restando el mayor menos el menor).
print('Ingresa diez numeros e imprimir el mayor, el menor y el rango del conjunto')
print()
n=int(input('Ingresa un numero: '))
cont=1
menor=n
mayor=n
while cont<10:
    n=int(input('Ingresa un numero: '))
    if n>mayor:
        mayor=n
    elif n<menor:
        menor=n
    cont=cont+1
rango=mayor-menor
print('El mayor numero ingresado es',mayor,'el menor',menor,'y el rango del conjunto es',rango)