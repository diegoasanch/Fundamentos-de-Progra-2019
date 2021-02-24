#Realizar un programa para ingresar desde el teclado un conjunto de números e
#informar los elementos ingresados menores a un valor ingresado previamente.
#Finalizar la lectura de datos con el valor -1.
print('Establezca un limite e imprimir los valores ingresados que sean menores al limite')
print()
lim=int(input('Ingrese el limite: '))
print()
menores=[]
n=int(input('Ingrese un numero: '))
while n!=-1:
    if n<lim:
        menores.append(n)
    n=int(input('Ingrese un numero: '))
print('Los valores ingresados menores a',lim,'son',menores)