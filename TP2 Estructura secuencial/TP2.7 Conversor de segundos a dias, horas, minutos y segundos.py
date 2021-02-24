#Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos.
#Por ejemplo, 200000 segundos equivalen a 2 días, 7horas, 33 minutos y 20 segundos.
print('Conversor de Segundos a Dias, Horas, Minutos y Segundos')
print()

segundos=int(input('Ingresa el tiempo a convertir en segundos: '))
Rsegundos=segundos%60

minutos=segundos//60
Rminutos=minutos%60

horas=minutos//60
Rhoras=horas%24

dias=horas//24
print()
print(segundos,'segundos equivalen a:',dias,'dias,',Rhoras,'horas,',Rminutos,'minutos y,',Rsegundos,'segundos.')
