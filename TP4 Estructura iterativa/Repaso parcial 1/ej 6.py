print('Ingrese numeros y conozca cuantos pares e impares ingreso, para terminar -1')
print()
n=int(input('Ingrese un numero: '))
if n==-1:
    print('No se ingreso ningun numero')
else:
    cantp=0
    canti=0
    while n!=-1:
        if n%2==0:
            cantp=cantp+1
        else:
            canti=canti+1
        n=int(input('Ingrese un numero: '))
    print()
    print('Se ingresaron',cantp,'numeros pares y',canti,'numeros impares')
