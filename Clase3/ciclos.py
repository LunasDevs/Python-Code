# numeros = [54, 58+5, 45, 12, 57, 84, 64, 25]

# # for numero in numeros:
# #     if numero > 50:
# #         print(numero)

# for numero in numeros:
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         print('-')


""" devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000,'years':5},
         {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000,'years':2},
         {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000,'years':3},
         {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000,'years':4},
         {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000,'years':5},
         {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000,'years':5},
         {'cc': 1547, 'nombre': 'David', 'salario': 2500000,'years':3},
         {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000,'years':6},
         {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000,'years':2},
         {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000,'years':1}]
 """
# for dev in devs:
#     print(dev['cc'])

# mostrar el mayor salario
# salario = 0

# for dev in devs:
#     x = dev['salario']
#     if x > salario:
#         salario = x
# print(salario)

#mostrar el nombre y la cedula de la persona con mayor salario:
# salario = 0
# nombre = str()
# cedula = str()

# for dev in devs:
#     x = dev['salario']
#     if x > salario:
#         salario = x
#         nombre = dev['nombre']
#         cedula = dev['cc']
# print('salario: ' + str(salario) + ' nombre: ' + str(nombre) + ' cc: ' + str(cedula))

# numeros = [54, 58+5, 45, 12, 57, 84, 64, 25]

# i = 0
# #imprimir numeros impares
# while i < len(numeros):
#     if i < 60:
#         x = numeros[i]
#     i+=1
# print(x)

#*********************    
# numeros = [54, 58+5, 45, 12, 57, 84, 64, 25]

#imprimir numeros
# while i < len(numeros):
#     print(numeros[i])
#     i+=1


""" i = 0
menor = 0
while i< len(numeros):
    if i == 0:
        menor = numeros[0]
    if menor < numeros[i]:
        menor = numeros[i]
    i+=1
print(menor) """


""" devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000,'years':5},
         {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000,'years':2},
         {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000,'years':3},
         {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000,'years':4},
         {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000,'years':5},
         {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000,'years':5},
         {'cc': 1547, 'nombre': 'David', 'salario': 2500000,'years':3},
         {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000,'years':6},
         {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000,'years':2},
         {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000,'years':1}] """

#desarrollador con menor experiencia
""" i = 0
dev_temp = {}

while i < len(devs):
    if i == 0:
        dev_temp = devs[0]
    if dev_temp ['years'] < devs[i]['years']:
        dev_temp = devs[i]
    i+=1
print(dev_temp) """

""" diccionario = {'a':{'nombre1':'Marco', 'edad1':31, 'lenguajes':{
                1:'Python',
                2:'C++',
                3:'Java',
                4:'PHP',
                5:'JavaScript',
                6:'C#'}
               },'b':{'nombre1':'Juan', 'edad1':21, 
               'lenguajes':{
                1:'Python',
                2:'C++',
                3:'Java'}
               }} """

""" for key in diccionario.keys():
    print(key) """

""" for dev in diccionario.values():
    print(dev) """

""" for key, value in diccionario.items():
    print(key)
    print(value) """

#numeros = [54, 58+5, 45, 12, 57, 84, 64, 25]

# sacar el número de la mitad
""" i = 0
while i < len(numeros):
    print(numeros[i])
    i+=0 """

# saltar elementos de 2 en 2

# iniciar desde la mitad en un ciclo for
""" i = 0
while i < len(numeros):
    
    print(numeros[i])
    i+=0 """

students = {'a': {'name':'Juan','notas':[3.1,4.2,4,3.9,3.2]}, 'j': {'name':'Jenny','notas':[4,3.7,4,4,4.2]},\
        'c': {'name':'Ana','notas':[4.1,4.7,4.1,4.9,4.2]}, 'y': {'name':'Pedro','notas':[4,3.7,4,4,4.2]},\
            'x': {'name':'Pablo','notas':[4,3.3,3.4,3.2,3.2]}, 'l': {'name':'Carlos','notas':[3.4,3.8,4.2,4,4.1]},\
                'v': {'name':'Maria','notas':[4.8,4.7,4.6,4.9,4.8]}, 'r': {'name':'Luisa','notas':[4.8,4.7,4.5,4.5,4.9]},\
                    'b': {'name':'Mario','notas':[2.4,3.2,3.1,3.4,4.2]}, 'g': {'name':'Fabio','notas':[2.4,3.2,3.1,3.4,4.2]}}

# promedio mas alto high_average y nombre del estudiante
# promedio mas bajo low_average
# nota mas alta de todas
# nota mas baja de todas

nombre = str()
prom = float()
i = 0

for i in students:
    promi = float(sum(students[i]['notas'])/5)
    if promi >= prom:
        prom = promi
        nombre = students[i]['name']
    else:
        prom = prom
print('El promedio es: '+ str(promi) + ' y su nombre es: ' + str(nombre))

