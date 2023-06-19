# -Crea una función llamada encontrar_maximo que tome una lista de números
# como parámetro y devuelva el número máximo de la lista.

def encontrarMaximo(lista):
    lista=[]
    n = 0
    c = 0
    suma = 0
    continuar = "si"
    while (continuar == "Si" or continuar == "Sí" or continuar == "SI" or continuar == "SÍ" or continuar == "sÍ" or continuar == "sI" or continuar == "sí" or continuar == "si"):
        n = input("Ingrese un número entero: ")
        if continuar and n.isdigit():
            lista.append(n)
            continuar = input("Desea continuar?: ")
        elif (not n.isdigit()):
            return("Usted a ingresado un caracter invadilo. Ingrese un número entero.")
        else:
            return("El bucle a terminado.")
        
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return (f"El maximo entre todos los valores ingresados es {maximo}.")

lista=[]
print(encontrarMaximo(lista))

