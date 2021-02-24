#Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene.
#Ejemplo: Si se ingresa 12345 debe imprimir 5.
print('Cuantos digitos contiene un numero ingresado')
n=int(input('Ingrese un numero: '))
cont=0
while n>0:
    cont=cont+1
    n=n//10
print('Su numero tiene',cont,'digitos de largo')