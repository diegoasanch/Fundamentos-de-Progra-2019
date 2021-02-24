#Realizar un programa para ingresar desde el teclado un conjunto de números e
#informar el último elemento ingresado en una posición par. Finalizar la lectura de
#datos con el valor -1.
#Ejemplos:
#Si la secuencia es 3 7 4 5 6 7 9 -1 el valor a informar es 7
#Si la secuencia es 3 7 4 5 -1 el valor a informar es 5
print('Imprime el ultimo valor par ingresado, ingrese -1 para terminar')
print()
n=int(input('Ingrese un valor: '))
v=1  #v= valor -1= impar, 1= par
if n!=-1:
    while n!=-1:
        v=v*-1
        if v==1:
            ultimopar=n
        n=int(input('Ingrese un valor: '))
    print()
    print('el ultimo valor ingresado en una posicion par es',ultimopar)
else:
    print('No ingreso ningun valor valido')