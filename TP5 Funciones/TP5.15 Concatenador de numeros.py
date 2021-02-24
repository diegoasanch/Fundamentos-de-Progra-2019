# Escribir una función que reciba como parámetros dos números enteros y devuelva la concatenación
# de ambos. Por ejemplo concatenar(123,456) devuelve 123456.

#funcion determina longitud del numero para multiplicar el primero por la unidad seguida de tantos
#ceros tenga de digitos el segundo termino
def multiplicador(entero):
    multi=1
    while entero>0:
        entero = entero // 10
        multi= multi * 10
    return multi

#verificador de positividad de un numero
def verifnum(tipo):
    print('>>> Ingrese',tipo,': ',end='')
    n=int(input())
    while n<0:
        print('\nNo ingreso un numero valido!!!')
        print('>>> Ingrese',tipo,': ',end='')
        n=int(input())
    return n

#funcion concateador
def concatenador(a,b,multi):
    unido= (a*multi)+b
    return unido
#programa principal
print('Concatenacion de numeros enteros')
A=verifnum('un numero') #ingreso de los numeros
B=verifnum('otro numero') 
multiplicador=multiplicador(B) #explicacion en la funcion
concatenado=concatenador(A,B,multiplicador)
print(concatenado)
