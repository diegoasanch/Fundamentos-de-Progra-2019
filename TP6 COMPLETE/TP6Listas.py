import ejercicios as TP6
import enunciados
import Basiclib

print('Bienvenido al portal de Ejercicios resueltos del \nTrabajo Practico 6: Funciones de Fundamentos de informatica :)\n')
input(' Presione enter para comenzar')
# Menu principal 
menu = True
while menu:
    print('\n+----------+----------+----------+-------- Menu Principal --------+----------+----------+----------+\n')
    print('Desea leer el listado de ejercicios? :',end='')
    listado = Basiclib.opcion() # Imprime el listado de los ejercicios
    if listado:
        enunciados.listado()
    print()
        
    # Listado de ejercicios, envia a la funcion del ejercicio correspondiente
    reint = True
    ops = ['-1','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
    op = input('Ingrese el ejercicio a ejecutar o (-1) para salir: ')
    while op not in ops:
        print('*** Opcion invalida, los ej van desde el 1 al 19 y (-1) para salir ***')
        op = input('Ingrese el ejercicio a ejecutar: ')
    # Salida del programa
    if op == '-1':
        reint = False
        print('*** Esta seguro que desea salir del programa? :',end='')
        menu = Basiclib.opcioninv()
    cont = 0 #contador para que muestre el enunciado siempre en la primera ejecucion y luego la pregunte
    en = True
    # Ejecucion del ejercicio correspondiente
    while reint:
        print()
        print('+----------+----------+----------+----------+----------+----------+----------+----------+----------+')
        print('                                       >>> Ejercicio',op,'<<<')
        if cont > 0:
            print('Desea leer el enunciado del ejercicio? :',end='')
            en = Basiclib.opcion()
        print()
        if op == '1':
            if en:
                enunciados.ej1()
            TP6.ej1()
            
        elif op == '2':
            if en:
                enunciados.ej2()
            TP6.ej2()
            
        elif op == '3':
            if en:
                enunciados.ej3()
            TP6.ej3()
            
        elif op == '4':
            if en:
                enunciados.ej4()
            TP6.ej4()
        
        elif op == '5':
            if en:
                enunciados.ej5()
            TP6.ej5()
            
        elif op == '6':
            if en:
                enunciados.ej6()
            TP6.ej6()
                 
        elif op == '7':
            if en:
                enunciados.ej7()
            TP6.ej7()
            
        elif op == '8':
            if en:
                enunciados.ej8()
            TP6.ej8()
            
        elif op == '9':
            if en:
                enunciados.ej9()
            TP6.ej9()
            
        elif op == '10':
            if en:
                enunciados.ej10()
            TP6.ej10()
            
        elif op == '11':
            if en:
                enunciados.ej11()
            TP6.ej11()
            
        elif op == '12':
            if en:
                enunciados.ej12()
            TP6.ej12()
            
        elif op == '13':
            if en:
                enunciados.ej13()
            TP6.ej13()
            
        elif op == '14':
            if en:
                enunciados.ej14()
            TP6.ej14()
            
        elif op == '15':
            if en:
                enunciados.ej15()
            TP6.ej15()
            
        elif op == '16':
            if en:
                enunciados.ej16()
            TP6.ej16()
            
        elif op == '17':
            if en:
                enunciados.ej17()
            TP6.ej17()
            
        elif op == '18':
            if en:
                enunciados.ej18()
            TP6.ej18()
        
        else:
            if en:
                enunciados.ej19()
            TP6.ej19()
    
        print()
        cont += 1
        print('Desea ejecutar de nuevo el mismo ej (1) o volver al menu principal (0)?: ',end='')        
        reint = Basiclib.opcion()
print('''
    fin del programa
+----------+----------+----------+----------+----------+----------+----------+----------+----------+''')
print('''
+----------+----------+----------+----------+----------+
+             Gracias por usar mis ej del TP6          +
+                                                      +
+ made with love by Diego.                             +
+ maric0 el que lo lea                                 +
+----------+----------+----------+----------+----------+''')