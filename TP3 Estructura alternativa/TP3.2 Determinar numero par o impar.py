#Leer un número entero A e imprimir un mensaje indicando si es par o impar
print('Determinar si un numero entero es par')
print()
num=int(input('Ingrese su numero entero: '))
resto=num%2
print()
if(resto==0):
    print('Su numero es par')
else:
    print('El numero ingresado es impar')
