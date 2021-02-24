#La sucesión de Fibonacci es una sucesión de números enteros donde cada término se obtiene como
#suma de los dos anteriores, siendo los dos primeros 1 y 1. Por lo tanto, Fib=1, 1, 2, 3, 5, 8, 13, 21....
#Realizar un programa que lea N e imprima los N primeros términos de esta sucesión, como así también la suma de
#los mismos.
N=int(input('Ingrese el numero de digitos de Fibonacci a calcular: '))
cont=2
ant1=1
ant2=0
sec=[1]
while cont<=N:
    fib=ant1+ant2
    ant2=ant1
    ant1=fib
    sec.append(fib)
    cont=cont+1
    ratio=ant1/ant2
print(sec)
print(ratio)