#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es par o impar.

numero = int(input("Ingrese un número cualquiera: "))

if (numero % 2 == 0):
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")