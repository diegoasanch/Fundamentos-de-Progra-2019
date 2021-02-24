#Realizar un programa que lea un número natural H e imprima un mensaje indicando si H es
#primo o no. Se dice que un número es primo cuando sólo es divisible por sí mismo y por la unidad.
H=int(input('Ingresa un numero para determinar si es primo: '))
a=(H/2)
dif=1
while dif>0.00001:
    raiz=((H/a)+a)/2
    dif=a-raiz
    a=raiz
#calculamos primero su raiz ya que si un numero no es primo al menos uno de sus divisores tiene que ser menor que
#raiz cuadrada 
cont=2
if H>1:
    while cont>0 and cont<=raiz:
        calc=H%cont
        if calc==0:
            divisor=cont
            cont=0
        elif cont==2:     #el contador comienza en dos para conseguir los n pares y lo llevamos a tres
            cont=cont+1
        else:             #luego el cont incrementa de dos en dos, para no probar de nuevo con cont pares
            cont=cont+2
    if H==4:
        divisor=2
        cont=0
else:
    cont=-1
if cont==0:
    print('El numero',H,'es divisible por',divisor)
elif cont==-1:
    print('Los numeros menores o iguales a 1 no se consideran primos')
else:
    print('El numero',H,'es primo')