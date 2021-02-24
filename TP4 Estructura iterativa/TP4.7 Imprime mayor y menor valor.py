#Realizar un programa para ingresar desde el teclado un conjunto de números y
#mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
#con un valor -1.
print('Ingrese numeros y conozca el mayor y menor de ellos, presione -1 para terminar')
print()
n=int(input('Ingrese el primer valor: '))
if n!=-1:
    menor=n
    mayor=n
    while n!=-1:
        if n<menor:
            menor=n
        elif n>mayor:
            mayor=n
        n=int(input('Ingrese otro valor: '))
    print('El numero mayor ingresado fue',mayor,'y el menor',menor)
else:
    print('No ingreso ningun numero valido')