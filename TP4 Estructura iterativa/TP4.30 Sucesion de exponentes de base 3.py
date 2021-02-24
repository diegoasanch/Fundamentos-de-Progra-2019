#Leer un número natural N. Calcular e imprimir los primeros N términos de la
#sucesión geométrica de razón 3, cuyos primeros términos son 1, 3, 9, 27, 81.....
#es decir 3^0, 3^1, 3^2, 3^3....
print('Sucesion de exponentes N con base 3')
N=int(input('Ingrese cuantos terminos desea calcular: '))
cont=0
while cont<N:
    exp=3**cont
    print('3^',cont,'=',exp)
    cont=cont+1
print('Esos son los primeros',N,'terminos de la sucesion de exponentes de base 3')