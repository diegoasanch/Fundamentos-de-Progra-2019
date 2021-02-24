print('Ingrese un numero y vealo en pantalla invertido')
print()
n=int(input('Ingrese un numero: '))
ind=0 #indicador de negatividad
inv=0
ingreso=n
if n==0:
    print('0 invertido es 0, duh')
elif n<0:
    n=n*(-1)
    ind=1
while n>0:
    ult=n%10
    n=n//10
    inv=(inv*10)+ult
if ind==1:
    inv=str(inv)+'-'
print(ingreso,'Invertido, es:',inv)