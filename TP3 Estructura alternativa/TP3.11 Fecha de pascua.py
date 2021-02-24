#La fecha de Pascua para un año cualquiera X puede determinarse mediante el
#siguiente algoritmo:
#· Calcular el resto de dividir X sobre 19 y llamarlo A.
#· Calcular el resto de dividir X sobre 4 y llamarlo B.
#· Calcular el resto de dividir X sobre 7 y llamarlo C.
#· Multiplicar A por 19, sumarle 24 y calcular el resto de dividir este resultado por 30. Este resto recibirá el nombre D.
#· Multiplicar B por 2, C por 4 y D por 6. Sumar los tres resultados y sumarle 5. Calcular el resto de dividir este último
#                                                                                           resultado por 7 y llamarlo E.
#· La fecha de Pascua se obtiene sumando los valores D y E, más la constante 22.
#· El resultado se expresa como una fecha dentro del mes de Marzo. Si el
#número es mayor que 31, entonces ese año Pascua se celebrará en el
#mes de Abril. Ejemplo: Un resultado 35 significa que Pascua cae el 4 de
#Abril (35 menos los 31 días del mes de Marzo es igual a 4).
#Preparar un programa que permita ingresar el año y calcule la fecha de Pascua.
print()
print('Cuando es pascua?')
op=1
while op==1:
    print()
    X=int(input('Ingrese el año: '))

    A=X%19
    B=X%4
    C=X%7
    D=(A*19+24)%30
    E=((B*2)+(C*4)+(D*6)+5)%7
    pascua=D+E+22
    
    if pascua<=31:
        print('En el año',X,'pascua sera el',pascua,'de marzo')
    else:
        print('En el año',X,'pascua sera el',pascua-31,'de abril')
    op=int(input('cont=1 salir=0: '))
while op==0:
    print('Felices Pascuas!')
    op=2

