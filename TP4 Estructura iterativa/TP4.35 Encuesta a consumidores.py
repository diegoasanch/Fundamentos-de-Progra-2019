#Se realizó una encuesta entre 100 consumidores. Por cada persona interrogada se ingresan dos valores:
#El primero indica la aceptación o no del producto A, mediante un 1 (acepta) o un 0 (no acepta). El segundo valor
#del par corresponde la producto B. Por ejemplo, el par (1,0) señala que el encuestado acepta el producto A pero
#no el B. Se solicita informar el porcentaje de consumidores que aceptan:
#· El producto A.
#· El producto B.
#· El producto A solamente.
#· El producto B solamente.
#· Ninguno de los dos.
#· Ambos productos.
print('Encuesta de producto')
cons=int(input('Ingrese la cantidad de personas a encuestar: '))
print()
print('acepto el producto=1 no acepto el producto=0')
print()
totalA=0
totalB=0
soloA=0
soloB=0
ambos=0
ninguno=0
pers=1
while pers<=cons:
    print('Consumidor',pers)
    A=int(input('Ingrese su opinion sobre el producto A: '))
    B=int(input('Ingrese su opinion sobre el producto B: '))
    if A==1 and B==0:
        soloA+=1
        totalA+=1
    elif A==0 and B==1:
        soloB+=1
        totalB+=1
    elif A==1 and B==1:
        ambos+=1
        totalA+=1
        totalB+=1
    else:
        ninguno+=1
    pers+=1
#porcentajes
porcA=(totalA/cons)*100
porcB=(totalB/cons)*100
porcsoloA=(soloA/cons)*100
porcsoloB=(soloB/cons)*100
porcambos=(ambos/cons)*100
porcninguno=(ninguno/cons)*100
print('Porcentaje de consumidores que escogieron:')
print()
print('El producto A:',porcA,'%')
print('El producto B:',porcB,'%')
print('Solo el producto A:',porcsoloA,'%')
print('Solo el producto B:',porcsoloB,'%')
print('Ambos productos:',porcambos,'%')
print('Ningun producto:',porcninguno,'%')