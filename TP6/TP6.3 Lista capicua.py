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
    largo= len(lista)
    pos= largo - 1
    evaluacion = largo//2
    cont=0
    while cont < evaluacion:
        if lista[cont] == lista[pos]:
            es_capicua = True
            cont = cont + 1
            pos = pos - 1
        else:
            cont = evaluacion+1
            es_capicua = False
    return es_capicua
        
#programa principal
print('Ingrese numeros entre el 1 el 20 a una lista y verifique si la misma es capicua')
milista=ingresodenum()
if milista == []:
    print('Lista vacia')
else:
    capicua=verificadorcapicua(milista)
    print(milista)
    if capicua == False:
        valor=' no'
    else:
        valor=''
    print('La lista'+valor+' es capicua')
