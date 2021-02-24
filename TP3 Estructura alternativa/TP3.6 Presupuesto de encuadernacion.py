#Una editorial determina el precio de un libro según la cantidad de páginas que
# contiene. El costo básico del libro es de $125, más $2,20 por página con encuadernación
# rústica. Si el número de páginas supera las 300 la encuadernación
# debe ser en tela, lo que incrementa el costo en $80. Además, si el número de
# páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación
# que incrementa el costo en $136. Desarrollar un programa que calcule el costo de
# un libro dado el número de páginas.

print()
print("Editorial Walrus' Books")
op=1
while op==1:
    print()
    print('Calculador de presupuesto de impresion')
    print()
    pag=int(input('Cuantas paginas contiene tu libro?: '))
    libros=int(input('Cuantos libros quieres imprimir?: '))
    if libros<1:
        #error de valor
        print('***Ingrese una cantidad valida de libros***presione x para reintentar')
    else:
        #basicos
        base=125
        Cpag=2.2
        tela=80
        especial=136
        #encuadernacion
        Erustico= base+(pag*Cpag)
        Etela= base+(pag*Cpag)+tela
        Eespecial= base+(pag*Cpag)+tela+especial
        
        if pag>0 and pag<=300:     #rustica
            enc='rustica'        #encuadernacion
            Cenc='Incluido'      #costo de encuadernacion
            total=Erustico               
        elif pag>300 and pag<=600: #tela
            enc='en tela'
            Cenc=tela
            total=Etela
        else:                       #especial
            enc='especial'
            Cenc=tela+especial
            total=Eespecial
        #programa en pantalla
        print()
        print('Presupuesto de su libro')
        print()
        print('Base:                      ',"{0:.2f}".format(base))
        print(pag,'Paginas:               ',"{0:.2f}".format(pag*Cpag))
        print('Enc',enc,':            ',Cenc)
        print('...................................................')
        print('Total x Libro         $ ',"{0:.2f}".format(total))
        print('Total x',libros,'Libros     $',"{0:.2f}".format(total*libros))          
    print()
    op=int(input('*Desea calcular otro presupuesto?* 1=si 0=no: '))
print('**Gracias por preferir walrus books!!1**')