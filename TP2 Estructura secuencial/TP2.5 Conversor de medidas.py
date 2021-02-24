#Leer una medida en metros e imprimir esta medida expresada en centímetros,
# pulgadas, pies y yardas. Los factores de conversión son:
#· 1 pie = 12 pulgadas
#· 1 yarda = 3 pies
#· 1 pulgada = 2,54 cm.
#· 1 metro = 100 cm.
print('Conversor de Metros a otras medidas')
print()
m = float(input('Ingrese medida en metros: '))
cm = m*100
pulgada = cm/2.54
pie = pulgada/12
yarda = pie/3
print()
print(m,'metro/s equivale a:')
print()
print("{0:.2f}".format(cm),'centimetro/s')
print("{0:.2f}".format(pulgada),'pulgada/s')
print("{0:.2f}".format(pie),'pie/s')
print("{0:.2f}".format(yarda),'yarda/s')
print()
input('presione enter para salir')