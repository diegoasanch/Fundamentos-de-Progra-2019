def ingresodenum(mi,ma):
    n = int(input())
    while n < mi or n > ma:
        print('Opcion invalida, debe ingresar un numero entre',mi,'y',ma)
        n = int(input('>Ingrese un numero: '))
    return n

# Ingreso de opcion si o no
def opcion():
    a = input()
    while a!= '1' and a!= '0' and a != 'si' and a != 'SI' and a != 'Si' and a!= 'S' and a!= 's' and a != 'no' and a != 'NO' and a != 'No' and a !='n' and a!='N':
        print('¡Opcion invalida!')
        a = input('¿Si o No? : ')
    if a == '1' or a == 'si' or a == 'SI' or a == 'Si' or a == 'S' or a == 's':
        op = True
    elif a == '0' or a == 'no' or a == 'NO' or a == 'No' or a== 'N' or a == 'n':
        op = False
    return op

def opcioninv():
    a = input()
    while a!= '1' and a!= '0' and a != 'si' and a != 'SI' and a != 'Si' and a!= 'S' and a!= 's' and a != 'no' and a != 'NO' and a != 'No' and a !='n' and a!='N':
        print('¡Opcion invalida!')
        a = input('¿Si o No? : ')
    if a == '1' or a == 'si' or a == 'SI' or a == 'Si' or a == 'S' or a == 's':
        op = False
    elif a == '0' or a == 'no' or a == 'NO' or a == 'No' or a== 'N' or a == 'n':
        op = True
    return op