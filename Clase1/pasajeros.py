# Un bus viaja a 30km/h en promedio, 90km
# recoger pasajeros demora 2 minutos por pasajero
# bajar pasajero demora 1 minuto

# Cuantos minutos demora el bus, dada una cantidad de pasajeros que se subieron
# y otra cantidad de pasajeros que se bajaron

a = float(input("Por favor ingrese el número de pasajeros abordados: "))
b = float(input("Por favor ingrese el número de pasajeros abordados: "))

def calcular_tiempo_recorrido(numero_abordados:int , numero_desc:int) -> float:
    pass
    velocidad = 30 # km/h
    distancia = 90 # km
    tiempo_pasajeros = ((numero_abordados * 2) + (numero_desc * 1))
    tiempo_bus = (((velocidad * distancia) / 60) + tiempo_pasajeros)
    return tiempo_bus

print("El tiempo total del bus es: " + str(calcular_tiempo_recorrido(a,b)))

