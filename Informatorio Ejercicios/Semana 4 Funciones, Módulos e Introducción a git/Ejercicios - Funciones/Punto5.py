# -Crea una función llamada es_divisible que tome dos números enteros como
# parámetros y devuelva Es divisible si el primer número es divisible por el
# segundo número, o No es divisible en caso contrario.

def esDivisible(num1,num2):
    if num1%num2 ==0:
        return(f"Los números {num1} y {num2}, si son divisibles.")
    else:
        return(f"Los números {num1} y {num2}, no son divisibles.")
    
num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
print(esDivisible(num1,num2))

