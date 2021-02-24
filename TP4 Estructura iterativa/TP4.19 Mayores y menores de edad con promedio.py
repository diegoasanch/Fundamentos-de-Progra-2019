#Leer un conjunto de números que representan edades de un grupo de personas,
#finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son
#menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de
#ambos grupos.
print('Ingrese edades, ingrese 999 para terminar')
print()
edad=int(input('Ingrese una edad: '))
mayor=0
contmayor=0
menor=0
contmenor=0
if edad!=999:
    while edad!=999:
        if edad>=18:
            mayor=mayor+edad
            contmayor=contmayor+1
        else:
            menor=menor+edad
            contmenor=contmenor+1
        edad=int(input('Ingrese una edad: '))
    if contmayor>0 and contmenor>0:
        prommayor=mayor/contmayor
        prommenor=menor/contmenor
        promgeneral=(mayor+menor)/(contmayor+contmenor)
        print('Se ingresaron',contmenor,'menores de edad y',contmayor,'mayores de edad.')
        print('El promedio de edad de los menores es de',prommenor,'años, el de los mayores es de',prommayor,'años')
        print('El promedio general es de',promgeneral,'años de edad')
    elif contmayor>0 and contmenor==0:
        prommayor=mayor/contmayor
        print('Se ingresaron',contmayor,'mayores de edad, y ningun menor de edad.')
        print('El promedio de edad es de',prommayor,'años')
    else:
        prommenor=menor/contmenor
        print('Se ingresaron',contmenor,'menores de edad, y ningun mayor de edad.')
        print('El promedio de edad es de',prommenor,'años')
else:
    print('***no se ingreso ninguna edad valida***')