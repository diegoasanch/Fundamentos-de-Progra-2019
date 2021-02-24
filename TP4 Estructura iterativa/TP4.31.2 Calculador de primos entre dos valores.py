#Utilizando el ejercicio TP4.31 este es un programa que calcula los numeros primos que extisten entre dos
#valores ingresados
print('Numeros primos entre dos valores')
A=int(input('Ingrese un valor: '))
B=int(input('Ingrese el otro valor: '))
cont=A
if A<=B:
    A=A
    B=B
else:
    C=B
    B=A
    A=C
primos=[]
cont=2
H=A
val=-1
while H<B:
    while cont>0 and cont<=H:
        calc=H%cont
        if calc==0:
            H=H+1
        if cont == H:
            cont=cont+1
        print(H)