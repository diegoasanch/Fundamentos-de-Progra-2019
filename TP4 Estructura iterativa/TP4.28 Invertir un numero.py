#Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el
#número invertido. Por ejemplo, si se ingresa 1234 debe mostrar 4321.
print('Invertir un numero ingresado')
n=int(input('Ingrese un numero: '))
inv=0
while n>0:
    n2=n%10
    inv=(inv*10)+n2
    n=n//10
print('Su numero invertido es:',inv)