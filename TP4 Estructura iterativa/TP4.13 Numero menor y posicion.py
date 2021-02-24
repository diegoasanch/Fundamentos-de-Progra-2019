#Leer diez números e imprimir el menor de ellos, indicando además el número de
#orden con que fue leído.
print('Ingrese 10 numeros, imprimir el menor y la posicion en la que fue leida')
n=int(input('Ingrese un numero: '))
menor=n
cont=1
pos=1
while cont<10:
    cont=cont+1
    n=int(input('Ingrese un numero: '))
    if n<menor:
        menor=n
        pos=cont
print('El menor numero ingresado fue',menor,'en la posicion',pos)