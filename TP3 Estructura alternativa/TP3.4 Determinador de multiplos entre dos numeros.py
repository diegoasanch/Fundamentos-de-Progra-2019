#Ingresar dos números enteros A y B. Desarrollar un programa que determine si
# A es múltiplo de B y si B es múltiplo de A. Imprimir mensajes aclaratorios.
print('Determinar si dos numeros A y B son multiplos entre ellos mismos')
print()
A=int(input('Ingrese el valor de A: '))
B=int(input('Ingrese el valor de B: '))
AmB=A%B
BmA=B%A
print()
if(AmB==0):
    print('A=',A,'es un multiplo de B=',B)
elif(BmA==0):
    print('B=',B,'es un multiplo de A=',A)
else:
    print('Los numeros A=',A,'y B=',B,'no son multiplos entre si')
