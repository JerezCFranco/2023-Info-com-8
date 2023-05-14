# -Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los
# elementos de la tupla.
def sumar(tupla):
    suma=0
    for i in tupla:
        suma+=i
    return suma

tupla_numeros=(1,2,3,4,5)
print(f"La suma de todos los elementos de la tupla es: {sumar(tupla_numeros)}.")
