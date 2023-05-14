#Escribir un programa que pida al usuario tres números y muestre por pantalla
#el mayor de ellos.

print("Se le solicitara ingresar tres números por pantalla.")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if (numero1>numero2 and numero1>numero3):
    print(f"El mayor de los tres es el primer número, el número {numero1}.")
elif (numero2>numero1 and numero2>numero3):
    print(f"El mayor de los tres es el segundo número, el número {numero2}.")
elif (numero1==numero2 and numero1==numero3):
    print("Los tres números ingresados son iguales.")
elif (numero1==numero2 and numero1>numero3):
    print("El primer y segundo número son iguales, y son mayores que el tercero.")
elif (numero2==numero3 and numero2>numero1):
    print("El segundo y tercer número son iguales, y son mayores que el primer número.")
else:
    print(f"El mayor de los tres es el tercer número, el número {numero3}.")
