#Calcular total compra con iva y descuento 10%

varticuloa = 10 #int(input("Por favor ingrese el valor del primer artículo: "))
varticulob = 30 #int(input("Por favor ingrese el valor del segundo artículo: "))
varticuloc = 60 #int(input("Por favor ingrese el valor del tercer artículo: "))
iva = 1.19

varticuloa = int(input("Por favor ingrese el valor del primer artículo: "))
varticulob = int(input("Por favor ingrese el valor del segundo artículo: "))
varticuloc = int(input("Por favor ingrese el valor del tercer artículo: "))
iva = float(input("Por favor ingrese el iva (terminos de porcentaje): "))

total = int(((varticuloa * iva) + (varticulob * iva) + (varticuloc * iva)) * 0.9)
print("El total de la compra es: " + str(total))