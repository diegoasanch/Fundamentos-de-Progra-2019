#Escribir un programa que imprima los múltiplos de 7 hasta el 3000
print('Imprime los multiplos de 7 hasta el 3000')
x=input('Presiona enter para comenzar:')
n=7
print(n)
while n<=3000:
    n=n+1
    while n%7==0:
        print(n)
        n=n+1
print('Esos son todos los multiplos de 7 hasta el 3000 :))')