#La sucesión de Fibonacci es una sucesión de números enteros donde cada término se obtiene como
#suma de los dos anteriores, siendo los dos primeros 1 y 1. Por lo tanto, Fib=1, 1, 2, 3, 5, 8, 13, 21....
#Realizar un programa que lea N e imprima los N primeros términos de esta sucesión, como así también la suma de
#los mismos.
N=int(input('Ingrese el numero de digitos de Fibonacci a calcular: '))
cont=1
ant1=1  #anterior 1
ant2=0  #anterior 2
print(cont,end=',')
while cont<N:
    fib=ant1+ant2
    ant2=ant1
    ant1=fib
    print(fib,end=',')
    cont=cont+1