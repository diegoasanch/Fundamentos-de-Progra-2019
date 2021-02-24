# Dados dos parámetros enteros A y B, obtener A^B (A elevado a la B) mediante
# multiplicaciones sucesivas, utilizando la función del ejercicio 1.

# Calculo del producto por sumas consecutivas
def calculoproducto(A,B):
    contr=B  #contador en reversa
    producto=0
    while contr>0:
        contr=contr-1
        producto=producto+A
    return producto
# Calculo de la potencia por productos consecutivos
def calculopotencia(A,B):
    if B==0:
        exp=1
    else:
        cont=2
        exp=A
        while cont<=B:
            exp= calculoproducto(exp,A)
            cont=cont+1
    return exp
# Programa principal
print('Calculo de potencia por medio de multiplicaciones')
a=int(input('Ingrese la base: '))
b=int(input('Ingrese el exponente: '))
potencia= calculopotencia(a,b)
print(a,'^',b,'=',potencia)