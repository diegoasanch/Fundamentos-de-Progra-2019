# Cargar dos listas de números A y B. Se solicita construir e imprimir tres nuevas
# listas C, D y E que contengan:
# · La concatenación de los valores pares de A con los impares de B.*
# · La concatenación de los valores pares de A con el reverso de los valores
# pares de B. ("valores pares" o "valores impares" se refiere a los elementos propiamente dichos y no a sus posiciones).
# · La intercalación de los elementos de A y B.

def ingresodenum(tamanio,num):
    lista = []
    print()
    print('Ingrese los valores de la lista',num,' y -1 para finalizar: ')
    for i in range(tamanio):
        n=int(input('Ingrese un numero: '))
        while n<1 or n>20:
            print('Error, debe ingresar un numero entre 1 y 20')
            n=int(input('Ingrese un numero: '))
        lista.append(n)
    return lista

## Concatenacion de los valores pares de A con los impares de B
# def concatparimpar(a,b):
#     largoa=len(a)
#     largob=len(b)
#     if largoa>=largob:
#         mayor=largoa
#     else:
#         mayor= largob
#     for i in range(mayor):
#         i
#         
# Intercalacion de los elementos de A y B
def intercal(a,b):
    inter = []
    for i in range(len(a)):
        if i < len(a):
            inter.append(a[i])
        if i < len(b):
            inter.append(b[i])
    return inter
        
#programa principal
print('Ingrese numeros entre el 1 el 20 a una lista')
#T=int(input('cuantos elementos desea ingresar en cada lista? : '))
A=ingresodenum(T,1)
B=ingresodenum(T,2)
D=intercal(A,B)
print()
print('lista A',A,'lista B',B)
print('Elementos de A y B intercalados',D)