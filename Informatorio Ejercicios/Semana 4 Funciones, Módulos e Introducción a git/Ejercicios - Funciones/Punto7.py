# -Crea una función llamada imprimir_pares que tome un número entero como
# parámetro y imprima todos los números pares desde 1 hasta ese número.

def imprimirPares(num):
    cont=0
    for i in range(1,num):
        if(i%2==0):
            cont+=1
    return cont
num=int(input("Ingrese un número entero: "))
print(imprimirPares(num))