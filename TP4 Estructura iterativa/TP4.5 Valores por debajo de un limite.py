#Realizar un programa para ingresar desde el teclado un conjunto de números e
#informar los elementos ingresados menores a un valor ingresado previamente.
#Finalizar la lectura de datos con el valor -1.
print('Establezca un limite e imprimir los valores ingresados que sean menores al limite')
print()
lim=int(input('Ingrese el limite: '))
print()
n=int(input('Ingrese un numero: '))
while n!=-1:
    if n<lim:
        print('El valor',n,'es menor a',lim)
    n=int(input('Ingrese un numero: '))
print('Fin del programa')