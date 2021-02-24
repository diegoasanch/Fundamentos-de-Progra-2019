print('Imprime en pantalla cuantos digitos tiene un numero ingresado')
n=int(input('Ingrese un numero: '))
incial=n
cont=0
if n<0:
    n=n*(-1)
while n>0:
    n=n//10
    cont=cont+1
print('El numero:',incial,'tiene',cont,'digitos')