#Leer dos números naturales A y B. Calcular A**B mediante productos sucesivos y
#mostrar el resultado. Tener en cuenta que A y B pueden ser nulos.
print('Ingresa dos numeros naturales A y B y calcula A elevado a la B mediante productos sucesivos')
A=int(input('Ingresa el valor de A: '))
B=int(input('Ingresa el valor de B: '))
cont=2
exp=A
if B!=0:
    while cont<=B:
        exp=exp*A
        cont=cont+1
    print(A,'^',B,'es=',exp)
else:
    print(A,'^',B,'es=',1)