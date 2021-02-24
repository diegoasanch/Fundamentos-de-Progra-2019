#Leer un número entero N y determinar si es un número natural (positivo y distinto de 0).
# Si lo es, imprimirlo junto con su doble. En caso contrario, imprimirlo junto con su triple.
print('Leer un numero entero N. Si N es natural, duplicarlo. De lo contrario, triplicarlo')
print()
N=int(input('Ingrese el valor de N: '))
print()
if(N>0):
    print('El numero ingresado es:',N,'y su doble es:',N*2)
elif(N<0):
    print('El numero ingresado es:',N,'y su triple es:',N*3)
else:
    print('El numero ingresado es cero, 0')
