# -Crea una función llamada es_palindromo que tome una cadena de texto como
# parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
# de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
# contrario.

def esPalindromo(palabra):
    palabra=palabra.lower()
    a = 0
    b = len(palabra) - 1
    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a+=1
            a-=1
        else:
            return False
    return True

palabra = input("Escriba una palabra y analizaremos si es Palíndromo: ")
if (esPalindromo(palabra)):
    print("La palabra ingresada es Palíndromo.")
else:
    print("La palabra ingresada no es Palíndromo.")