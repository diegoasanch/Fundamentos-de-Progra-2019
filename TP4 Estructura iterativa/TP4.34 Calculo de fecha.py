#Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y
#un número entero N que representa una cantidad de días. Realizar un programa
#que calcule e imprima la nueva fecha que resulta de sumar N días a la fecha
#dada. Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 9 de
#la práctica 3
print()
print('Calculador de fechas')
op=1
while op==1:
    print()
    dia=int(input('Ingrese el dia: '))
    mes=int(input('Ingrese el mes: '))
    anio=int(input('Ingrese el año: '))
    fecha=[dia,mes,anio]
    #bisiesto
    bis4=anio%4
    bis100=anio%100
    bis400=anio%400
    print()
    if bis4==0:
        if bis100==0 and bis400!=0:
            bis=0
        else:
            bis=1
    else:
        bis=0
    calcb=0
    #Validez de la fecha
    if dia < 1:
        validez=0
    elif (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia<=31:
        validez=1
    elif (mes==4 or mes==6 or mes==9 or mes==11) and dia<=30:
        validez=1
    elif mes==2 and bis==0 and dia <=28:
        validez=1
    elif mes==2 and bis==1 and dia <=29:
        validez=1
    else:
        validez=0
    if validez==0:
        print('La fecha',fecha,'no es valida')
        op=int(input('Reintentar=1 Salir=0: '))
    #calculador de fecha
    else:
        N=int(input('Ingrese los dias a sumar: '))
        suma=dia+N 
        while ((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and suma>31) or ((mes==4 or mes==6 or mes==9 or mes==11) and suma>30) or (mes==2 and bis==0 and suma>28) or (mes==2 and bis==1 and suma>29):
            if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10):
                suma=suma-31
                mes=mes+1
            elif mes==12:
                suma=suma-31
                mes=1
                anio=anio+1
            elif (mes==4 or mes==6 or mes==9 or mes==11):
                suma=suma-30
                mes=mes+1
            elif mes==2 and bis==0:
                suma=suma-28
                mes=mes+1
            elif mes==2 and bis==1:
                suma=suma-29
                mes=mes+1
        fecha2=[suma,mes,anio]
        print('La fecha',fecha,'mas',N,'dias resulta en la fecha',fecha2)
        op=int(input('Reintentar=1 Salir=0: '))
print()
print('***Gracias por usar el calculador de fechas*** :)')
