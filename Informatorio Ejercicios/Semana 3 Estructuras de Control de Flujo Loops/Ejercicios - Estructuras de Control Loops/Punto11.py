# -Escribe un programa que pida al usuario un número y calcule su factorial.
# Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
# de 4 es 4! = 4 × 3 × 2 × 1 = 24.
numero = int(input("Ingrese un número entero: "))
factorial=1
for i in range(1,numero+1):
    factorial*=i
print(f"El factorial de {numero}, es {factorial}.")