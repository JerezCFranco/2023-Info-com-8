# -Crea una función llamada es_par que tome un número como parámetro y
# devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
# devuelva Es impar o No es par.

def esPar(num):
    if num%2==0:
        return(f"El número {num} es par.")
    else:
        return(f"El número {num} es impar.")

num=int(input("Ingrese un número entero: "))
print(esPar(num))