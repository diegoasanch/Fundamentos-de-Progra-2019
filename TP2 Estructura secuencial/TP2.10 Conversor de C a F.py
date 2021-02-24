#Desarrollar un programa que solicite una temperatura expresada en grados centígrados y la
#imprima convertida a grados Fahrenheit, tal que:  C= 5/9*(F-32)
print('Conversor de Centigrados a Farenheit o Vice versa')
print()
print('Para convertir de C a F ingrese: 1')
print('Para convertir de F a C ingrese: 2')
print()
conv=int(input('Que conversion desea realizar?: '))
temp=float(input('Ingrese la temperatura a convertir: '))

CaF=(temp*9/5)+32
FaC=5/9*(temp-32)

if(conv==1):
    print()
    print('Celcios a Farenheit')
    print()
    print(temp,'grados Celcios equivale a',CaF,'grados Farenheit')
elif(conv==2):
    print()
    print('Farenheit a Celcios')
    print()
    print(temp,'grados Farenheit equivale a',FaC,'grados Celcios')
else:
    print('Ingrese un tipo de conversion valido')
