import func
import Basiclib
import enunciados

def cargalista1():
    print('Ingresa los numeros a cargar en la lista, ingresa -1 para finalizar la carga\n')
    MI = 1
    MA = 20
    v = func.cargaconlimites(MI,MA)
    return v

def ej1():
    print('Carga de numeros entre 1 y 20 en una lista\n')
    v = cargalista1()
    print()
    print('Lista Cargada',v)
    
def ej2():
    v = cargalista1()
    print()
    print('Lista',v)
    suma = func.sumadelista(v)
    print('Suma de todos los elementos de la lista',suma)
    
def ej3():
    v = cargalista1()
    capicua = func.verifcapicua(v)
    print()
    if capicua:
        print('La lista',v,'es capicua')
    else:
        print('La lista',v,'no es capicua')
        
def ej4():
    v = cargalista1()
    print()
    print('Lista original',v)
    func.invertirposimpar(v)
    print('Lista con los elementos ubicados en posicion impar invertidos:')
    print(v)
    
def ej5():
    print('Busqueda secuencial\n')
    print('Ingresa los numeros a cargar en la lista, ingresa -1 para finalizar la carga\n')
    v = func.carganormal()
    print('Lista',v)
    n = int(input('>Ingrese un numero para buscarlo en la lista: '))
    enc = func.busquedasecuencial(n,v)
    print()
    if enc == -1:
        print(enc,'El numero solicitado:',n,'no pertenece a la lista')
    else:
        print('El numero',n,'se encuentra en la lista en la posicion',enc)
    
def ej6():
    print('Busqueda binaria\n')
    print('Ingresa los numeros a cargar en la lista, ingresa -1 para finalizar la carga\n')
    v = func.carganormal()
    if v == []:
        print('No se cargo ningun elemento a la lista :s')
    elif len(v) == 1:
        print('La lista',v,'tiene un solo elemento, no se puede ordenar (que esperabas?)')
    else:
        print('\nLista',v)
        print('Al utilizar busqueda binaria primero debemos ordenar la lista')
        print('Desea usar ordenamiento secuencial (1) u ordenamiento por burbujeo (2)?: ',end='')
        op = Basiclib.ingresodenum(1,2)
        if op == 1:
            func.ordenadorsecuencial(v)
        else:
            func.ordenadorburbujeo(v)
        print('\nLista ordenada',v)
        n = int(input('>Ingrese un numero para buscarlo en la lista: '))
        enc = func.busquedabinaria(n,v)
        print()
        if enc == -1:
            print(enc,'El numero solicitado:',n,'no pertenece a la lista')
        else:
            print('El numero',n,'se encuentra en la lista en la posicion',enc)
        
def ej7():
    yr = func.inicializacion(12)
    print('Ingrese el numero de legajo y fecha de cumpleaños de los estudiantes')
    print('Para finalizar la carga de datos ingrese -1 como legajo\n')
    leg = int(input('Ingrese el numero de legajo: '))
    while leg != -1:
        input('Ingrese el dia: ')
        print('Ingrese el mes: ',end='')
        m = Basiclib.ingresodenum(1,12)
        input('Ingrese el año: ')
        yr[m-1] = yr[m-1]+1
        print()
        leg = int(input('Ingrese el numero de legajo: '))
    suma = func.sumadelista(yr)
    print()
    if suma == 0:
        print('No se cargo ningun cumpleaños :(')
    else:
        print('Total de cumpleaños:',suma)
        func.impresioncumple(yr)
        mi,ma = func.busquedaminmax(yr)
        meses_max = func.busquedasecuenciallist(ma,yr)
        if len(meses_max) == 1:
            print('mes con mas cumpleaños',meses_max[0],'con',ma,'cumpleaños')
        else:
            func.impresionmeses_max(meses_max,ma)

def ej8():
    input('Presione enter para comenzar')
    MI, MA = 0, 100
    v = func.cargarandomhasta0(MI,MA)
    if v == []:
        print('El generador de numeros fallo en su unica tarea y el primer numero que genero fue 0 :s :(')
    else:
        print('Lista generada',v)
        mi,ma = func.busquedaminmax(v)
        n_min = func.busquedasecuenciallist(mi,v)
        n_max = func.busquedasecuenciallist(ma,v)
        print('El menor numero de la lista es el',mi,'esta en la/s posicion/es',n_min)
        print('El mayor numero de la lista es el',ma,'esta en la/s posicion/es',n_max)

def ej9():
    print('Ingrese los valores a cargar en la lista, ingrese -1 para terminar la carga')
    v = func.carganormal()
    v2 = func.comp_menorigual(v)
    print()
    print('Lista    ',v)
    if v == []:
        print('La lista esta vacia e.e no hay elementos para comparar')
    elif len(v) == 1:
        print('La lista tiene un solo elemento, por lo tanto no se puede realizar ninguna comparacion :(')
    else:
        print('resultado',v2)
    
def ej10():
    print('#@#@#@#@#@#@#@#@#@#@#@#@#@')
    print('Ejercicio en construccion')
    print('#@#@#@#@#@#@#@#@#@#@#@#@#@')
    
def ej11():
    print('Ingrese los valores a cargar en la lista, ingrese -1 para terminar la carga')
    A = func.carganormal()
    print('Lista:',A)
    if A == []:
        print('No cargaste ningun numero, do you think this is a joke??')
    else:
        tipo_ord = func.deteccion_de_orden(A)
        #tipo_0 determina el tipo de ordenamiento de la lista 0= desordenada, 1= ascendente, 2= descendente, 3= todos los elementos iguales
        print()
        if tipo_ord == 0:
            print('La lista esta desordenada, para continuar primero debemos ordenarla')
            print('Desea ordenar la lista de forma ascendente (1) o descendente (0)?: ',end='')
            ascend = Basiclib.opcion()
            if ascend: 
                func.ordenadorburbujeo(A)
                tipo_ord = 1
            else:
                func.ordenadorburbujeodes(A)
                tipo_ord = 2
            print('\nLista ordenada:',A)
        elif tipo_ord == 1 or tipo_ord == 2:
            print('La lista ya esta ordenada! bien ahi')
        else:
            print('Todos los elementos de la lista son iguales, easy peasy insertar el numero')    
    N = int(input('Ingrese el numero a insertar en la lista: '))
    func.insercion_ordenada(N,A,tipo_ord)
    print('\nLista final:',A)
    print('\nDesea agregar otro numero a la lista?: ',end='')
    op = Basiclib.opcion()
    while op:
        N = int(input('Ingrese el numero a insertar en la lista: '))
        func.insercion_ordenada(N,A,tipo_ord)
        print('Nueva lista',A)
        print('\nDesea agregar otro numero a la lista?: ',end='')
        op = Basiclib.opcion()
        
def ej12():
    print('Ingrese los valores a cargar en la lista, ingrese -1 para terminar la carga')
    v = func.carganormal()
    print('\nLista:',v)
    # item 1
    print('\n- Cociente entre producto de los elementos en pos. par entre la suma de los elementos en pos. impar:\n')
    sub_par, sub_imp = func.separacion_par_impar(v)
    prod = func.productodelista(sub_par)
    suma = func.sumadelista(sub_imp)
    if suma == 0:
        print('No se puede realizar la operacion ya que la suma de los elementos en posicion impar es = 0')
    else:
        cociente = prod / suma
        print('Producto',prod,'/ suma',suma,'=',cociente)
    # item 2
    print('\n- Suma del primer elemento con el ultimo, el segundo con el penultimo... and so on and so forth\n')
    suma2 = func.suma_extremos(v)
    print('Lista de sumas',suma2)
    #item 3
    print('\n- Comparacion de los elementos laterales de la lista"\n')
    lats = func.comparacion_laterales(v)
    if lats == []:
        print('Ningun elemento de la lista cumple la condicion de tener ambos elementos laterales iguales :((((')
    elif len(lats) == 1:
        if lats[0] == len(v)-1:
            lateral = v[lats[0]-1]
        else:
            lateral = v[lats[0]+1]
        print('El unico elemento de la lista que tiene ambos laterales iguales es el:',v[lats[0]])
        print('Y sus laterales son:',lateral)
    else:
        print('Los elementos que tienen sus laterales iguales son')
        func.impresion_laterales(v,lats)  
    
def ej13():
    print('Ingrese los valores a cargar en la lista, ingrese -1 para terminar la carga')
    v = func.carganormal()
    print('\nLista:',v)
    if v == []:
        print('La lista esta vacia :c')
    elif len(v) == 1:
        print('La lista tiene un solo elemento (o sea esta ordenada (?) maybe?)')
    else:
        tipo = func.deteccion_de_orden(v)
        if tipo == 0:
            print('La lista esta desordenada')
        elif tipo == 1:
            print('La lista esta ordenada de forma ascendente')
        elif tipo == 2:
            print('La lista esta ordenada de forma descendente')
        else:
            print('Todos los elementos de la lista son iguales')
    
def ej14():
    print('Ingrese los valores de la lista 1: ')
    v1 = func.carganormal()
    print('\nAhora ingrese los valores de la lista 2:')
    v2 = func.carganormal()
    print('Lista 1',v1)
    print('Lista 2',v2)
    print()
    if v1 == []:
        print('No se puede eliminar un elemento de una lista si esta esta vacia :/')
    elif v2 == []:
        print('Lista 1 - lista 2 =',v1,'oh wait, no hay nada que quitarle a la lista 1')
    else:
        func.eliminacion_v1menosv2(v1,v2)
        print('Lista 1 - lista 2 =',v1)

    
def ej15():
    print('Ingrese los valores de la lista M:')
    M = func.carganormal()
    print('\nIngrese los valores de la lista N:')
    N =func.carganormal()
    ordM = func.deteccion_de_orden(M)
    ordN = func.deteccion_de_orden(N)
    if ordM == 1 and ordN == 1:
        print('depinga mano, ambas listas ya estan ordenadas :D')
    elif ordM != 1 and ordN != 1:
        print('Ambas listas estan desordenadas brother :( pero tranqui, yo las ordeno')
        func.ordenadorburbujeo(M)
        func.ordenadorburbujeo(N)
    else:
        print('Alguna de las listas esta desordenada, pero no te voy a decir cual es, solo la ordenare')
        if ordM != 1:
            func.ordenadorburbujeo(M)
        else:
            func.ordenadorburbujeo(N)
    print('Lista M',M)
    print('Lista N',N)
    MN = func.intercalador(M,N)
    print('Lista MN',MN)

def ej16():
    print('¡Adivina el valor secreto!')
    print()
    option = 1
    enunciados.ej16_instrucciones()
    punt, nomb = [0],[0] # Inicializacion de las listas de puntajes
    while option:
        func.busquedadelnum(punt,nomb,16)
        print('¿Desea volver a jugar?',end='')
        option = Basiclib.opcion()
        print()
    print('Gracias por jugar Adivina el valor secreto :)')


    
def ej17():
    print('¡Adivina el valor secreto!')
    print()
    option = 1
    enunciados.ej17_instrucciones()
    punt, nomb = [0],[0] # Inicializacion de las listas de puntajes
    while option:
        func.busquedadelnum(punt,nomb,17)
        print('¿Desea volver a jugar?',end='')
        option = Basiclib.opcion()
        print()
    print('Gracias por jugar Adivina el valor secreto :)')
    
def ej18():
    N = int(input('Ingrese la cantidad de numeros al azar a generar: '))
    while N < 0:
        print('No se puede generar una cantidad negativa de numeros :s')
        N = int(input('Intenta con otro numero: '))
    SECUENCIAS = func.secuencias(N)
    print('Lista generada',SECUENCIAS)
    
def ej19():
    N = int(input('Ingrese la cantidad de numeros al azar a generar: '))
    while N < 0:
        print('No se puede generar una cantidad negativa de numeros :s')
        N = int(input('Intenta con otro numero: '))
    SECUENCIAS = func.secuencias(N)
    print('Lista generada',SECUENCIAS)
    print()
    sec_mas_larga, comienzo_sec = func.secuencia_mas_larga(SECUENCIAS)
    if len(comienzo_sec) == 1:
        print('La secuencia mas larga es de',sec_mas_larga,'digitos:')
    else:
        print('Las secuencias mas largas tienen',sec_mas_larga,'digitos:')
    for i in range(len(comienzo_sec)):
        func.impresiondesec(SECUENCIAS,comienzo_sec[i],sec_mas_larga)
        print()
