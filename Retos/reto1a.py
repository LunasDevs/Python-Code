#Se envía la bienvenida y se solicita el usuario
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario_inp = input("Por favor ingrese su usuario: ")
#usuario_inp = '51743'
usuario = int(usuario_inp)
#Variables para validar el capcha y se convierten a entero para poder efectuar operaciones aritméticas
sumando1 = int(usuario_inp[-3:])
sumando2 = int(usuario_inp[-2])
captcha = sumando1 + sumando2
#print(f"captcha {captcha}")

#Variables para las 3 operaciones solicitadas en el captcha, se convierten a entero cada dígito para poder operarlas
operando1 = int(usuario_inp[0])#5
operando2 = int(usuario_inp[1])#1
operando3 = int(usuario_inp[-3])#7
operando4 = int(usuario_inp[-1])#3
#print(f" operando1 {operando1} operando2 {operando2} operando3 {operando3}")

#Se valida el usuario vs el codigo del mi grupo de fundamentos de programación
if usuario == 51743:
    #contrasena_inp = '34715'  
    contrasena_inp = input("Por favor ingrese su contraseña: ")
    contrasena = int(contrasena_inp[::-1])
    #print(f"Reverso Contraseña{contrasena}")
    if usuario == contrasena:
        # Se solicita al usuario que ingrese el captcha y se convierte a entero para poder compararlo
        captcha_inp = int(input(f"Por favor ingrese el Captcha: {sumando1} + {sumando2}: "))
        #print(f"captcha_inp {captcha_inp}")
        if captcha == captcha_inp:
            operaciona = operando3 - operando4
            operacionb = (((operando3 + operando2) * operando4) % operando1 )
            operacionc = round(((operando3 * operando1) - operando4 ) / (operando2 + operando3))
            #print(f"resultados operacion A: {operaciona} , operacion B: {operacionb} , operacion C: {operacionc}")
            print("Sesión iniciada")
            exit(0)
        else:
            #no ingresó correctamente el captcha
            print("Error")
            exit(0)
    else:
        #no ingresó correctamente la contraseña
        print("Error")
        exit(0)
else:
    #ingreso un usuario diferente al código de fundamentos de programación
    print("Error")
    exit(0)