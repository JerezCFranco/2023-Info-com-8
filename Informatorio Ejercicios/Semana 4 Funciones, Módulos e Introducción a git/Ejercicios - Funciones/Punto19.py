# -Crea una función llamada es_bisiesto que tome un año como parámetro y
# devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
# es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
# divisible por 400.

def esBisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        return (f"El año {año} si es biciesto.")
    else:
        return (f"El año {año} no es biciesto.")

print("Bievenido, se le solicitara ingresar un año para analizar si es biciesto.")
año = int(input("Ingrese un año para analizar: "))
print(esBisiesto(año))