# -Crea una función llamada suma que tome dos números como parámetros y
# devuelva la suma de ellos.

def suma(num1,num2):
    suma=num1+num2
    return suma

print("Bienvenido, se le solicitara ingresar dos números para comprobar el funcionamiento de la funcion suma.")
num1=int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
print(f"La suma de el primer y segundo número es: {suma(num1,num2)}.")