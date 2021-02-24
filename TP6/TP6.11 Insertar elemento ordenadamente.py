# Dada una lista ordenada de números llamada A y un nuevo número N, desarrollar un programa que agregue el elemento N dentro de la lista A,
# respetando el ordenamiento existente. El programa deberá detectar automáticamente si el ordenamiento es ascendente o descendente antes de
# realizar la inserción.

#Funcion ingreso de numeros
def ingresodenum():
    print('Ingrese numeros del 1 al 20, y -1 para finalizar la carga de datos')
    lista = []
    n=int(input('Ingrese un numero: '))
    while n!=-1:
        if n>=1 and n<=20:
            lista.append(n)
        else:
            print('### Error, debe ingresar un numero entre 1 y 20### ')
        n=int(input('Ingrese un numero: '))
    return lista

# Ingreso de valor a ingresar
def ingresodev():
    n=int(input('Ingrese el valor a insertar a la lista: '))
    while n<1 or n>20:
        print('### Error, debe ingresar un numero entre 1 y 20 ###')
        n=int(input('Ingrese un numero: '))
    return n

#Funcion ordenar la lista por seleccion
def ordenador(lista,t):
    largo = len(lista)
    for i in range(largo-1):
        for j in range(i+1, largo):
            if t == 1:
                if lista[i] > lista[j]:
                    aux = lista[j]
                    lista[j] = lista[i]
                    lista[i] = aux
            else:
                if lista[i] < lista[j]:
                    aux = lista[j]
                    lista[j] = lista[i]
                    lista[i] = aux
    return lista

# Insercion del valor
def insercion(lista,n,t):
    lista.append(n)
    ordenador(lista,t)
    return
    
# Ingreso del tipo de ordenamiento deseado
def tipodeord():
    t = input('Quiere ordenar la lista de forma ascendiente (a) o descendiente (d)? : ')
    while t!= 'a' and t!='d':
        print('Opcion invalida!!!!')
        t = input('(a)ascendiente o (d)escendiente? : ')
    if t == 'a':
        opcion = 1
    else:
        opcion = -1
    return opcion
    
# Programa principal
print('Ingrese numeros en una lista, recibala ordenada y luego ingrese un valor para insertar respetando el orden')
print()
milista = ingresodenum()
print()
print('Lista ingresada')
print(milista)
tipo = tipodeord()                   #Ingreso de como se quiere ordenar la lista
milista = ordenador(milista,tipo)    #Funcion de ordenar de la manera escogida
print()
print('Lista ordenada', milista)
v = ingresodev()
insercion(milista,v,tipo)
print('lista con el nuevo termino', milista)