#-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es positivo, negativo o cero.

numero_entero = int(input("Ingrese un número entero: "))
if numero_entero>=1:
    print("El número ingresado es positivo.")
elif numero_entero<0:
    print("El número ingresado es negativo.")
else:
    print("El número ingresado es cero.")