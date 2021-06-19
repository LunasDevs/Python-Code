palabra = "Un texto de varias palabras"
print(palabra[0:5])
#palabra  = 5

# tuplas: se usan para datos fijos. no son modificables, ocupan menos espacio en memoria:
# 
# listas: son mutables, permiten agregar mas valores. ocupan mas espacio en memoria
#  https://recursospython.com/guias-y-manuales/listas-y-tuplas/

notas  = [  3.1, 4.2, 4, 3.9, 3.2, 3.5, 4.1, 3.3]
#indices    0    1    2    3    4   5   6    7
notas = 'una palabra'

i = 0
#print(len(notas))
while i < len(notas):
    notas[i] = notas[i] * 2
    print(notas[i])
    i+=1