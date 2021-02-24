#Desarrollar un programa que imprima los números impares comprendidos entre
#1 y 1000.
print('Ve en pantalla todos los numeros impares entre 1 y 1000')
print()
n=input('Presiona enter para comenzar: ')
x=1
while x<=1000:
    if x%2!=0:
        print(x)
    x=x+1
print('Esos son todos los impares entre 1 y 1000 :)')
