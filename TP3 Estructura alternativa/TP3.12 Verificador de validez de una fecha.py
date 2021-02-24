#Leer tres números correspondientes al día, mes y año de una fecha e imprimir
#un mensaje indicando si la fecha es válida o no.
print()
print('Ingrese una fecha')
print()
dia=int(input('Ingrese el dia: '))
mes=int(input('Ingrese el mes: '))
anio=int(input('Ingrese el a#o: '))
if mes==(1 or 3 or 5 or 7 or 8 or 10 or 12) and dia<=31:
    validez=1
elif mes==(4 or 6 or 9 or 11) and dia<=30:
    validez=1
elif mes==2 and dia <=28:
    validez=1
else:
    validez=0
if validez==1:
    print('La fecha',dia,'/',mes,'/',anio,'es valida :)')
else:
    print('La fecha ingresada',dia,'/',mes,'/',anio,'no es valida :(')