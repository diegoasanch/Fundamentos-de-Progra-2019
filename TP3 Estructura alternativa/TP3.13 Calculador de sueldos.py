#Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
#base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
#el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es
#casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
#También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social:
#3%, Sindicato: 3%

#Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil
#(‘s’ o ‘c’). Se debe informar: (reemplazar los 9 por los
#valores que correspondan)

#Estado Civil: Soltero/Casado
#Sueldo básico              Antigüedad   Descuentos   Importe
# $ 999.99                    99 años                + 999.99
#                                 Jubilación - 999,99
#                                Obra Social - 999,99
#                                  Sindicato - 999,99
#                                          ------------
#                       Sueldo Neto            999,99
print()
print('Calculador de sueldo')
print()
basico=float(input('Ingrese el sueldo basico: '))
ant=int(input('Ingrese la antigüedad en la empresa: '))
estcv=str(input('Estado civil soltero=s casado=c: '))
if estcv=='s':
    importe=basico*(0.05*ant)
    civil='Soltero'
else:
    importe=basico*(0.07*ant)
    civil='Casado'
    
jubilacion=basico*0.11
obras=basico*0.03
sindicato=basico*0.03
neto=basico+importe-jubilacion-obras-sindicato
print()
print('Estado Civil:',civil)
print('Sueldo básico              Antigüedad   Descuentos   Importe')
print('$',basico,'                   ',ant,'años                 +',"{0:.2f}".format(importe))
print('                        Jubilacion        -',"{0:.2f}".format(jubilacion))
print('                        Obra Social       -',"{0:.2f}".format(obras))
print('                        Sindicato         -',"{0:.2f}".format(sindicato))
print('                                      ------------------')
print('                        Sueldo Neto      $ ',"{0:.2f}".format(neto))