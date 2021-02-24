# Leer dos listas de números M y N, ambas ordenadas de menor a mayor. Generar
# e imprimir una tercera lista que resulte de intercalar los elementos de M y N. La
# nueva lista también debe quedar ordenada, sin utilizar ningún método de ordenamiento.

#Ingreso de numeros
def ingresodenum():
    lista = []
    n = int(input('Ingrese un numero: '))
    while n != -1:
        lista.append(n)
        n = int(input('Ingrese un numero: '))
    if lista != []:
        ordenador(lista)
    return lista

# Ordenador de lista de forma ascendiente por el metodo de seleccion
def ordenador(lista):
    largo = len(lista)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return

# Intercalador de listas
def intercalador(a,b):
    largoa = len(a)
    largob = len(b)
    interc = []
    if largob < largoa:
        c = a
        a = b
        b = c
        largoa = len(a)-1
        largob = len(b)-1
    i , j = 0, 0
    while i <= largoa and j <= largob:
        if a[i] <= b[j]:
            interc.append(a[i])
            if i <= largoa:
                i += 1
        else:
            interc.append(b[j])
            if j <= largob:
                j += 1
    return interc

#Programa principal
print('Ingrese dos listas (el programa las ordenara por ti) y recibe una tercera lista con los elementos de ambas listas intercalados\n')
print('Ingrese los elementos de la primera lista, finaliza con -1')
M = ingresodenum()
print('Ingrese los elementos de la segunda lista, finaliza con -1')
N = ingresodenum()
MN = intercalador(M,N)
print('Lista 1',M,'lista 2',N)
print('Listas intercaladas',MN)