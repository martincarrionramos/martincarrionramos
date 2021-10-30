#PostWork 1 de Martin Carrión
#Curso básico de Python

print("Bienvenido a la calculadora de tarjeta de crédito")
print()
print("Por favor, proporcione la siguiente información:")
nombre=input("¿Cuál es la institución bancaria? ")
tasa_int=float(input("¿Cuál la tasa de interés anual? "))
deuda=float(input("¿Cuál es el monto de la deuda al mes anterior? "))
pago=float(input("¿Cuál es el pago que realizará? "))
cargos=float(input("¿Cuáles son los cargos a su tarjeta en este mes? "))
print()
print("Le confirmo los datos que me ha proporcionado:")
print("Su tarjeta {} está sujeta a una tasa de interés anual de {}%.".format(nombre,tasa_int))
print("Su deuda al cierre del mes anterior es de ${}, y planea pagar ${}.".format(deuda,pago))
print("Finalmente, su tarjeta acumuló nuevos cargos por un total de ${}.".format(cargos))
print()
if (pago>deuda):
    print("El pago máximo que usted puede realizar es por el monto total de la deuda.")
    print("En este caso, usted ha excedido ese monto. Le solicito proporcionar un monto")
    print("igual o menor a la deuda total para usar adecuadamente esta calculadora.")
elif (pago==deuda):
    print("Usted está liquidando su deuda del mes anterior. Por lo tanto,")
    print("su nuevo saldo es de ${}".format(cargos))
else:
    int_mes=tasa_int/12/100
    deuda_act=(deuda-pago)*(1+int_mes)
    cierre_mes=deuda_act+cargos
    print("Después de realizar el pago, su deuda es de ${}".format(deuda_act))
    print("Considerando los cargos de ${}, su nuevo saldo es de ${}".format(cargos,cierre_mes))

print()
print("¡Esperamos que esta información le sea útil!")
print()
