#Realizar un programa para ingresar desde el teclado un conjunto de números e
#informar si la cantidad de elementos es impar o par, sin utilizar contadores.
#Finalizar la lectura de datos con el valor -1. 
print('Determina si la cantidad de elementos es par o impar sin usar contador, ingrese -1 para terminar')
print()
n=int(input('Ingrese un valor: '))
v=1  #v= valor -1= impar, 1= par
if n!=-1:
    while n!=-1:
        v=v*-1
        n=int(input('Ingrese un valor: '))
    if v==-1:
        cant='impar'
    else:
        cant='par'
    print()
    print('Usted ingreso una cantidad',cant,'de valores')
else:
    print('No ingreso ningun valor valido')