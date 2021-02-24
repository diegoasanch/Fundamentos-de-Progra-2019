#Dados dos parámetros numéricos, calcular y devolver el resultado de la multiplicación de ambos utilizando sólo sumas.
# Funcion multiplicacion
def calculoproducto(A,B):
    contr=B  #contador en reversa
    producto=0
    while contr>0:
        contr=contr-1
        producto=producto+A
    return producto

# Programa principal
print('Calculo de multiplicacion por medio de sumas')
a=int(input('Ingrese un numero: '))
b=int(input('Ingrese el otro numero: '))
prod=calculoproducto(a,b)
print(a,'*',b,'=',prod)