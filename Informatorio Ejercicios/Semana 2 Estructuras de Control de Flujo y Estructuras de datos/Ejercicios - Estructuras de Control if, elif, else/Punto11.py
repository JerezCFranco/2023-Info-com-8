#Escribir un programa que pida al usuario dos números y muestre por pantalla
#la suma de ellos solo si ambos son pares.

print("Se le solicitara ingresar dos números por pantalla.")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if ((num1%2==0) and (num2%2==0)):
    suma=num1+num2
    print(f"Ambos números son pares, y su suma es igual a {suma}.")
else:
    print("Ambos números no son pares, no se realizara la suma.")
