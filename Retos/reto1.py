#Se envía la bienvenida 
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Se definen las variables
usuariop = int(51743)
contrasenap = int(34715)
#Variables para validar el capcha y se convierten a entero para poder efectuar operaciones aritméticas
sumando1 = str(usuariop)[-3:]
sumando2 = str(usuariop)[-2]
captchap = int(sumando1) + int(sumando2)

#Variables para las 3 operaciones solicitadas en el captcha, se convierten a entero cada dígito para poder operarlas
operando1 = int(str(usuariop)[0])#5
operando2 = int(str(usuariop)[1])#1
operando3 = int(str(usuariop)[-3])#7
operando4 = int(str(usuariop)[-1])#3

operaciona = operando3 - operando4
operacionb = (((operando3 + operando2) * operando4) % operando1 )
operacionc = round(((operando3 * operando1) - operando4 ) / (operando2 + operando3))

usuario = int(input("Por favor ingrese su usuario: "))
if usuario == usuariop:
    contrasena = int(input("Por favor ingrese su contraseña: "))
    if contrasena == contrasenap:
        captcha = int(input("Por favor ingrese el Captcha " + sumando1 + " + " + str(operacionc) + " = " )) #operacionc tambien se puede reemplazar por str(operaciona), str(operacionb) ó sumando2
        if captcha == captchap:
            print("Sesión iniciada")
            exit(0)
        else:
            print("Error")
            exit(0)
    else:
        print("Error")
        exit(0)
else:
    print("Error")
    exit(0)