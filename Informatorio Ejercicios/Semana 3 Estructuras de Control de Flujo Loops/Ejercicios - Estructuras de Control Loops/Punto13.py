# -Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de asteriscos con esa cantidad de filas.
# *
# **
# ***
# ****
# *****
print("¡Bienvenido! en este programa ingresara un número y se graficara un triángulo de asteriscos con la cantidad dada.")
numero=input("Ingrese un número: ")
if numero.isdigit():
    numero=int(numero)
    for i in range(numero+1):
        print("*"*i)
else:
    print("Usted a ingresado un caracter invalido.")


