#Una inmobiliaria paga a sus vendedores un salario de $800, más una
#comisión de $50 por cada venta realizada, más el 5% del valor de esas
#ventas. Realizar un programa que imprima el número del vendedor y el
#salario que le corresponde en un determinado mes. Se leen el número
#del vendedor, la cantidad de ventas que realizó y el valor total de las mismas. 
print('Inmobiliaria Diego')
print()
print('Calculador de Sueldos')
print()
vendedor=input('Ingrese identificacion del Vendedor: ')
cant=int(input('Ingrese el numero de ventas: '))
mes=input('Ingrese el mes actual: ')
ventas=float(input('Ingrese el monto total de las ventas en el mes: '))
base=int(input('Ingrese salario base: '))
comision=50*cant
beneficio=0.05*ventas
total=base+comision+beneficio
print()
print('El salario del vendedor',vendedor,'para el mes de',mes,'corresponde a:')
print()
print('numero de ventas:    ',cant)
print()
print('Sueldo base_________________$',base)
print('comision por ventas__________$',comision)
print('beneficio por ventas________  $',beneficio)
print('_________________________________')
print('TOTAL                                      $   ',total)
