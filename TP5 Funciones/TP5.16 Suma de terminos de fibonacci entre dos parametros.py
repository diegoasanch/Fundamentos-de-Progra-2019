# Realizar una función que calcule y devuelva la sumatoria de los términos de la sucesión de Fibonacci
# entre dos números de término dados, los que se reciben como parámetros.

#funcion calculo de fibonacci
def fibonacci(minimo,maximo):
    ant1=1  #anterior 1
    ant2=0  #anterior 2
    fib=1
    suma=0
    while fib<=maximo:
        if fib>=minimo and fib<=maximo:
            suma=suma+fib
        fib=ant1+ant2
        ant2=ant1
        ant1=fib
    return suma

#verificador de positividad de un numero
def verifnum(tipo):
    print('>>> Ingrese',tipo,': ',end='')
    n=int(input())
    while n<0:
        print('\n****Ingrese un numero >=0****')
        print('>>> Ingrese',tipo,': ',end='')
        n=int(input())
    return n

#programa principal
print('Suma de los terminos de la sucesion de fibonacci entre dos limites')
A=verifnum('el limite inferior') #ingreso de los numeros
B=verifnum('el limite superior')
sumatoria=fibonacci(A,B)
print(sumatoria)