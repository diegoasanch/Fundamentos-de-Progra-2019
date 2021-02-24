#Realizar un programa para ingresar desde el teclado un conjunto de números e
#informar en forma separada la cantidad de elementos pares e impares ingresados.
#Finalizar la lectura de datos con el valor -1.
print('Contador de pares e impares, ingrese -1 para terminar')
print()
n=int(input('Ingrese un valor: '))
contpar=0
contimpar=0
if n!=-1:
    while n!=-1:
        if n%2==0:
            contpar=contpar+1
        else:
            contimpar=contimpar+1
        n=int(input('Ingrese un valor: '))
    print()
    print('Usted ingreso',contpar,'numeros pares y',contimpar,'numeros impares')
else:
    print('No ingreso ningun valor valido')