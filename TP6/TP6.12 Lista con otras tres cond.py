# Leer una lista de números V. Luego se solicita:
#    · Calcular el producto de los elementos de subíndice par y dividirlo por la suma de los elementos de subíndice impar,
#     sólo si esta suma es distinta de cero. Imprimir la lista leída y el resultado calculado, o un mensaje de error en caso
#      de no poder realizar la operación.
#    · Generar e imprimir otra lista tal que su primer elemento contenga la  suma del primero más el último elemento de la
#     lista V; el segundo elemento contenga la suma del segundo más el penúltimo de V, etc. La
#     nueva lista contendrá la mitad de los elementos de la lista original.
#    · Imprimir un listado de aquellos elementos de V que cumplan con la condición de tener iguales sus dos elementos laterales
#     (el anterior y el siguiente). Si ninguno cumple esta condición, se imprimirá una leyenda aclaratoria. Considerar que los
#     extremos de la lista se encuentran unidos, de modo que el último elemento se encuentra antes que el primero, y que el
#     primer elemento se encuentra después del último.

def ingresodenum():
    lista = []
    n = int(input('Ingrese un numero: '))
    while n!= -1:
        lista.append(n)
        n = int(input('Ingrese un numero: '))
    return lista

#Producto y division
def productoydivision(lista):
    largo = len(lista)
    producto = 1
    suma = 0
    for i in range(0,largo,2):
        producto = producto * lista[i]
    for i in range(1,largo,2):
        suma = suma + lista[i]
    if suma == 0:
        print('La suma de los elementos de subindice impar es 0, por lo tanto no se puede realizar la operacion! :( ')
    else:
        division = producto / suma
        print('Producto de los indices par',producto,'/ suma de los indices impar',suma,'=',division)
    return
    
#Suma de los extremos
def sumadeextremos(lista):
    sumex = []
    largo = len(lista)
    pos = largo-1
    for i in range(largo//2):
        suma = lista[i] + lista[pos]
        sumex.append(suma)
        pos = pos - 1
    print('La suma de los extremos de la lista incrementando y disminuyendo en 1, es',sumex)
    return
        
#Verificacion de los laterales iguales
def lateralesiguales(lista):
    later = []
    largo = len(lista)
    for i in range(largo):
        if i == 0:
            lati = lista[largo-1]
            latd = lista[i+1]
        elif i == largo-1:
            lati = lista[i-1]
            latd = lista[0]
        else:
            lati = lista[i-1]
            latd = lista[i+1]
        if lati == latd:
            later.append(i)
    if later == []:
        print('Ningun elemento de la lista cumple con la condicion de que ambos laterales sean iguales')
    else:
        imprimirlaterales(later,lista)
    return

def imprimirlaterales(later,lista):
    print('Los siguientes elementos tienen ambos laterales iguales')
    print('Posicion   Elemento   Laterales')
    for i in range(len(later)):
        if later[i] == len(lista)-1:
            lateral = lista[(later[i])-1]
        else:
            lateral = lista[(later[i])+1]
        print(later[i],' -------- ',lista[later[i]],' -------- ',lateral)
    print()
    return
    
# Programa principal
print('Cargar una lista y hacer los calculos del TP6. ej 12')
v = ingresodenum()
print('Lista ingresada',v)
print()
productoydivision(v)
sumadeextremos(v)
lateralesiguales(v)