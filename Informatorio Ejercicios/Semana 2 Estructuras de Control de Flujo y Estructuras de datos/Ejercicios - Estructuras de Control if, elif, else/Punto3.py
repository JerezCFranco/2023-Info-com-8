#Escribir un programa que pida al usuario dos números y muestre por pantalla
#cuál de ellos es mayor.

print("Se le pedira ingresar dos números.")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1>numero2:
    print(f"El mayor entre ambos es {numero1}.")
else:
    print(f"El mayor entre ambos es {numero2}.")