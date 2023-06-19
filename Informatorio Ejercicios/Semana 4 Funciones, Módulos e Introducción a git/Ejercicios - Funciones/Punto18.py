# -Crea una función llamada calcular_mayor_diferencia que tome una lista de
# números como parámetro y devuelva la mayor diferencia entre el numero mas
# alto y el numero mas bajo en la lista.

def mayor(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return max

def menor(lista):
    min = lista[0]
    for x in lista:
        if x < min:
            min = x
    return min

def calcularMayorDif(lista):
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
            return("Usted a ingresado un caracter invadilo. Ingrese un número entero.")
        else:
            return("El bucle a terminado.")
    MayorDif = mayor(lista)-menor(lista)
    return (f"La diferencia entre el número maximo y el minimo en la lista, es de {MayorDif}.")

lista=[]
print(calcularMayorDif(lista))