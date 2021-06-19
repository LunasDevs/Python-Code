cod_pais = str ( input("Por favor ingrese el código de país "))
codigo   = int (cod_pais.removeprefix('+'))
print(f"codigo {codigo}")
i = "h"

cel_integer = int( input("Por favor ingrese el número de Celular: "))
print(f"cel_integer {cel_integer}") 

if  codigo >= 30 and codigo <= 49 or codigo >= 350 and codigo <= 429 :
    cel_encriptado = str(i) + hex(cel_integer)
else :
    cel_encriptado = hex(cel_integer)

print(f"Celular encriptado: {cel_encriptado}")