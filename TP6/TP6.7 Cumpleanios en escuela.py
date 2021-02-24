# Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año, con el propósito de ofrecerles un agasajo especial en su día.
# Desarrollar un programa que lea el número de legajo y fecha de nacimiento (día, mes y año) de cada uno de los alumnos que concurren a dicha
# escuela. La carga finaliza con un número de legajo igual a -1. Emitir un informe donde aparezca -mes por mescuántos alumnos cumplen años a lo
# largo del año. Imprimir también una leyenda que indique cuál es el mes con mayor cantidad de cumpleaños.
def ingresodenum(minimo,maximo,param):
    print('Ingrese el',param,end=': ')
    n = int(input())
    while n < minimo or n > maximo:
        print('Debe ingresar un numero entre',minimo,'y',maximo)
        print('Ingrese el',param,end=': ')
        n = int(input())
    return n 

def ingresodedatos():
    mes = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    cont= 0
    l= int(input('Ingrese el numero de legajo: '))
    while l !=-1:
        m = ingresodenum(1,12,'mes')
        mes[m] = mes[m] + 1
        cont = cont + 1
        l= int(input('Ingrese el numero de legajo: '))
    return mes
    
def impresion(mes,minimo,maximo):
    print('Mes ----------- Cumpleañeros')
    for i in range(minimo,maximo):
        if mes[i] > 0:
            print(' ',i,'--------------',mes[i])
    return

def mayor(mes):
    mayor = 0
    mayores = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        if mes[i] > mayor:
            mayor = mes[i]
    for i in range(1,13):
        if mes[i] == mayor:
            mayores[i] = mes[i]
        largo = len(mayores)
    impresion(mayores,0,largo)
            
    return
    
#programa principal
fechas = ingresodedatos()
impresion(fechas,1,13)
print('El/ los meses con mayor cantidad de cumpleañeros es/son:')
mayor(fechas)