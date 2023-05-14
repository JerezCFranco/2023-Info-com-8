import random
intentos = 0
numero_x = float(random.randint(1,100))
print("¡Bienvenido a este juego!")
while intentos<8:
    intentos+=1
    print(f"Intente adivinar el número x, este es su intento N° {intentos}, de 8 intentos.")
    numero_usuario = input("Ingrese un número: ")
    
    if numero_usuario.isdigit():
        None
    else:
        print ("Usted a ingresado una letra o un número no entero, no se le descontara un intento. Ingrese un número nuevamente.")
        intentos-=1
        print("")
        continue
    numero_usuario = float(numero_usuario)
    if numero_usuario==numero_x:
        print(f"¡Felicidades!, usted adivino el número x en  su intento N°{intentos}.")
        print("")
        break
    elif numero_usuario>numero_x:
        print("El número ingresado es mayor al número x.")
        print("")
    elif numero_usuario<numero_x:
        print("El número ingresado es menor al número x.")
        print("")
else:
    print("Usted se quedo sin intentos, el programa finalizara.")

