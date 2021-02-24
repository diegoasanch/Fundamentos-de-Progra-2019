#Leer un número natural M. Calcular e imprimir:
#· La sumatoria de los números naturales menores o iguales que M.
#· La productoria de los números naturales mayores o iguales que M y menores que M*2.
print('Ingrese un numero M, calcular e imprimir la sumatoria de todos los naturales <= que M')
print('y el producto de todos los naturales >= que M y menores que M*2')
print()
M=int(input('Ingrese un numero natural M: '))
suma=0
producto=M
cont=1
while cont<=M:                #suma la suma anterior mas el numero del contador hasta llegar a al valor de M inclusive
    suma=suma+cont
    cont=cont+1
while cont>M and cont<M*2:    #producto, multiplica el producto anterior (comenzando en M) por 
    producto=producto*cont    #el numero del contador hasta llegar a M*2 sin tomarlo
    cont=cont+1
print('Los suma de todos los naturales <= a',M,'es=',suma)
print('El producto de todos los naturales >=',M,' y < a',M*2,'es=',producto)