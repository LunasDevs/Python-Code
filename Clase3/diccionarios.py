# diccionario = {'clave':'valor'}
# diccionario = {'nombre1':'Marco', 'edad1': 31, \
#                'nombre2':'Ana', 'edad2': 25, 
#                'lenguajes': {1: 'Phython', 2:'C++'}}

# print(diccionario['nombre1'])
# print(diccionario['edad2'])
# print(diccionario['lenguajes'][1])
# print(len(diccionario))
# print(len(diccionario['lenguajes']))

autos = {'autos':{
        1:{'marca':'Tesla',
           'modelos':{
               1:'Model S',
               2:'Model E',
               3:'Model X',
               4:'Model Y',
               }
           },
        2:{'marca':'Toyota',
           'modelos':{
               1:'Fortuner',
               2:'Prado',
               3:'Tundra',
               4:'Corola',
               }
           },
        3:{'marca':'Range Rover',
           'modelos':{
               1:'Evoque',
               2:'Defender',
               }
           },
        4:{'marca':'Mazda',
           'modelos':{
               1:'Mazda 3',
               2:'Mazda 2',
               3:'CX 30',
               }
           },
        5:{'marca':'Audi',
           'modelos':{
               1:'A7',
               2:'A5',
               3:'A3',
               }
           }
        }
        }

#print(autos['autos'])
#print(autos['autos'][4]['modelos'])
#print(len(autos['autos'][4]['modelos']))

m1 = len(autos['autos'][1]['modelos'])
m2 = len(autos['autos'][2]['modelos'])
m3 = len(autos['autos'][3]['modelos'])
m4 = len(autos['autos'][4]['modelos'])
m5 = len(autos['autos'][5]['modelos'])

print(max(m1,m2,m3,m4,m5))

