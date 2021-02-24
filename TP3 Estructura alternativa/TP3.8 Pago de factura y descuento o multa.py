#Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga su factura
# dentro de los primeros 10 días del mes siguiente, tiene un descuento de $120 o del 2%
# de la factura, lo que resulte menor. Si paga en los siguientes 10 días del mes deberá pagar
# el importe original de la factura, mientras que si paga después del día 20 deberá abonar
# una multa de $150 o del 10% de su factura, lo que resulte mayor. Desarrolle un programa
# que lea el número del cliente y el total de la factura, y emita un informe donde conste el
# número del cliente y los tres importes que podrá abonar según la fecha de pago.
print()
print('Raptor inc.')
op=1
while op==1:
    print()
    dia=int(input('Ingrese el dia del mes: '))
    if dia<1 or dia>31:
        print('***INGRESE UNA FECHA VALIDA***')
    else:
        cliente=input('Ingrese su ID de Cliente: ')
        total=float(input('Ingrese el importe total a facturar: $ '))
        if total<=0:
            print('***INGRESE UN MONTO VALIDO***')
        else:
            print()
            print('Fecha:',dia,'                        ID Cliente:',cliente)
            print('........................................................................................')
            print('El importe total de su factura es de  $  ',total)
            if dia<=10:
                desc=total*0.02
                if desc<120:
                    print('Por su pago temprano obtendra un 2% de descuento')
                    print('........................................................................................')
                    print('Total a pagar:     $',total-desc)
                else:
                    print('Por su pago temprano obtendra $120 de descuento')
                    print('........................................................................................')
                    print('Total a pagar:     $',total-120)        
            elif dia>10 and dia<=20:
                print('........................................................................................')
                print('Total a pagar:     $',total)
                print('Debera pagar la totalidad de su factura.')    
            else:
                multa=total*0.1
                if multa>150:
                    print('Por su pago retrasado debera pagar una multa del 10% de su factura')
                    print('........................................................................................')
                    print('Total a pagar:     $',total+multa)
                else:
                    print('Por su pago retrasado debera pagar una multa de $150')
                    print('........................................................................................')
                    print('Total a pagar:     $',total+150)
    print()
    op=int(input('Ingrese 1 para reiniciar o 0 para salir :'))
print('***Gracias por usar la calculadora de factura***')