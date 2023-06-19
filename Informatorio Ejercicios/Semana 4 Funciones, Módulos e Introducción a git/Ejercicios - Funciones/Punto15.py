# -Crea una función llamada contar_palabras que tome una cadena de texto
# como parámetro y devuelva el número de palabras que contiene. Se considera
# que las palabras están separadas por espacios.

def contarPalabras(cadena):
    cadena_lista = cadena.split(" ")
    return(f"El texto contiene {len(cadena_lista)} palabras.")

cadena=input("Escriba una cadena de texto: ")
print(contarPalabras(cadena))