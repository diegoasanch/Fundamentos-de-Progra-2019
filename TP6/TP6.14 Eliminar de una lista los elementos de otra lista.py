# Eliminar de una lista de números enteros los valores que se encuentren en una
# segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
# resultante.

# Carga de lista
def ingresodenum():
    lista = []
    n=int(input('Ingrese un numero: '))
    while n!=-1:
        if n>=0:
            lista.append(n)
        else:
            print('Error, debe ingresar un numero mayor o igual a 0')
        n=int(input('Ingrese un numero: '))
    return lista

# Eliminacion de los terminos
def eliminador(v,e):
    for i in range(len(e)):
        len(v) -1
        for j in range((len(v)-1),-1,-1):        
            if e[i] == v[j]:
                del v[j]
    return v

# Programa principal
print('Ingrese dos listas, los elementos de la segunda lista que se encuentren en la primera seran eliminados')
print('Ingrese los valores de la primera lista\n')
a = ingresodenum()
print('Ingrese los valores de la segunda lista\n')
b = ingresodenum()
print('\nLista 1',a)
print('\nLista 2',b)
c = eliminador(a,b)
print('\nLista 1 sin los valores de Lista 2',c)