# -Crea una función llamada promedio que tome una lista de números como
# parámetro y devuelva el promedio de esos números.

def Promedio(lista):
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
    print(f"Los lista de números obtenidos es: {lista}.")
    return(f"Y el promedio de estos es de {suma/c}.")

lista=[]
print(Promedio(lista))