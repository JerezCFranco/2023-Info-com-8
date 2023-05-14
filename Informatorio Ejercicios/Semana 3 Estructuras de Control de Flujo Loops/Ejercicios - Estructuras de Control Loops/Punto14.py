# -Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
cont=-1
print("¡Bienvenido! en este programa ingresara un número y se graficara un triángulo de asteriscos con la cantidad dada.")
numero=input("Ingrese un número: ")
if numero.isdigit():
    numero=int(numero)
    for i in range(numero+1):
        cont+=1
        print(str(cont)*i)
else:
    print("Usted a ingresado un caracter invalido.")

