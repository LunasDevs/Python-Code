# def verificar_mayor(edad1, edad2, edad3, edad4):
#     if edad1 > edad2 and edad1>edad3 and edad1> edad4:
#         print(edad1)
#     elif edad2 > edad1 and edad2 > edad3 and edad2 > edad4:
#         print(edad2)
#     elif edad3 > edad1 and edad3 > edad2 and edad3 > edad4:
#         print(edad3)
#     elif edad4 > edad1 and edad4 > edad2 and edad4 > edad3:
#         print(edad4)

def verificar_mayor(edad1, edad2, edad3, edad4):
     if edad1 > edad2 > edad3 > edad4:
         print(edad1)
     elif edad2 > edad3 > edad4:
         print(edad2)
     elif edad3 > edad4:
         print(edad3)
     else:
         print(edad4)

verificar_mayor(15, 48, 45, 48)
verificar_mayor(65, 58, 45, 65)