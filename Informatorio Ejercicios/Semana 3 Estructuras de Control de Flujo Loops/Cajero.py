
print("Bienvenido al cajero, tiene 3 intentos para ingresar su contraseña correctamente.")
contraseña = int(input("Ingrese su contraseña: "));
intentos = 0;

while intentos<3:
    intentos+=1
    if (contraseña==443):
        print("Contraseña correcta, ingresando al sistema.")
        break
    elif(intentos<3):
        print("Contraseña incorrecta, vuelva a intentarlo.")
        contraseña = int(input("Ingrese su contraseña: "));
    else:
        print("Limite de intentos excedido, bloqueando cuenta.")
