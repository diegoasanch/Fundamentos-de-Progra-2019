# Determinar si una lista es capicúa.

#funcion ingreso de valores
def ingresodenum():
    lista = []
    n=int(input('Ingrese un numero: '))
    while n!=-1:
        if n>=1 and n<=20:
            lista.append(n)
        else:
            print('Error, debe ingresar un numero entre 1 y 20')
        n=int(input('Ingrese un numero: '))
    return lista

#funcion capicua
def verificadorcapicua(lista):
    pos= len(lista) - 1
    evaluacion = len(lista)//2
    for i in range(evaluacion):
        if lista[i] == lista[pos]:
            pos -= 1
        else:
            es_capicua = False
            break
    else:
        es_capicua = True
    return es_capicua
        
#programa principal
print('Ingrese numeros entre el 1 el 20 a una lista y verifique si la misma es capicua')
milista=ingresodenum()
if milista == []:
    print('La lista esta vacia')
else:
    capicua=verificadorcapicua(milista)
    print(milista)
    if capicua == False:
        print('La lista no es capicua')
    else:
        print('La lista es capicua')
