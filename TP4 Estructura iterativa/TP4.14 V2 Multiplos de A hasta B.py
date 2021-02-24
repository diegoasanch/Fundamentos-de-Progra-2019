#Escribir un programa que imprima los múltiplos desde un valor hasta otro
print('Imprime los multiplos de un valor A hasta el B')
A=int(input('Ingrese el valor de A: '))
B=int(input('Ingrese el valor de B: '))
print(A)
cont=A
while cont<=B:
    cont=cont+1
    while cont%A==0:
        print(cont)
        cont=cont+1
print('Esos son todos los multiplos desde',A,'hasta el',B,':))')