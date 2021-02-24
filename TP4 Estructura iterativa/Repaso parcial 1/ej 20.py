print('Calculo de cociente por restas sucesivas')
A=int(input('Ingrese el dividendo: '))
B=int(input('Ingrese el divisor: '))
if A<B:
    print('Ingrese un dividendo mayor o igual al divisor')
elif B==0:
    print('No puede dividirse por 0')
else:
    resto=A
    coc=0
    while resto>=B:
        resto=resto-B
        coc=coc+1
    print()
    print('Dividendo:',A,'Divisor:',B)
    print('Cociente:',coc,'Resto:',resto)
        