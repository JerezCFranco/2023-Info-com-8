# -Escribe un programa que pida al usuario una lista de números separados por
# comas y calcule su promedio.
lista=[]
n = 0
c = 0
suma = 0
continuar = "si"
while (continuar == "Si" or continuar == "Sí" or continuar == "SI" or continuar == "SÍ" or continuar == "sÍ" or continuar == "sI" or continuar == "sí" or continuar == "si"):
    n = input("Ingrese un número entero: ")
    if continuar and n.isdigit():
        n=int(n)
        c=c + 1
        suma=suma + n
        lista.append(n)
        continuar = input("Desea continuar?: ")
    elif (not n.isdigit()):
        print("Usted a ingresado un caracter invadilo. Ingrese un número entero.")
    else:
        print("El bucle a terminado.")
print(f"Los lista de números obtenidos es: {lista}.")
print(f"Y el promedio de estos es de {suma/c}.")


