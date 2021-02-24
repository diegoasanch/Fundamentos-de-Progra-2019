#Leer cien números e imprimir su promedio
print('Ingrese 100 numero y conozca su promedio')
cont=0
suma=0
while cont<=100:
    cont=cont+1
    print('Ingrese el valor numero',cont,end='')
    n=int(input(': '))
    suma=suma+n
prom=suma/100
print('El total de los valores es',suma,'y su promedio',prom)