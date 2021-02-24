#Conversor de binario a decimal
print(' Conversor de Binario a Decimal')
print()
op=1
while op==1:
    bi=int(input('Ingrese un numero binario de cuatro cifras: '))
    #calculos, d=digito r=resto
    d0=bi%10
    r0=bi//10
    d1=r0%10
    r1=r0//10
    d2=r1%10
    r2=r1//10
    d3=r2%10

    dec=(d3*2**3)+(d2*2**2)+(d1*2**1)+(d0*2**0)
    print()
    print('Su numero binario',bi,'equivale a',dec,'en numeros decimales')
    print()
    op=int(input('Desea realizar otro calculo? si=1 no=0: '))
print('*gracias por usar la calculadora* :)')