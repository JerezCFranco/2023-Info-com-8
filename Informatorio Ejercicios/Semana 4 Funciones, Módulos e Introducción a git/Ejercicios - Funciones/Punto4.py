# -Crea una función llamada es_capicua que tome un número como parámetro y
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.

def esCapicua(num):
    if num>=0:
        if str(num)== str(num)[::-1]:
            return(f"El número {num} es capicúa.")
        else:
            return(f"El número {num} no es capicúa.")
    else:
        return("El número ingresado debe ser positivo.")

num=int(input("Ingrese un número positivo: "))    
print(esCapicua(num))