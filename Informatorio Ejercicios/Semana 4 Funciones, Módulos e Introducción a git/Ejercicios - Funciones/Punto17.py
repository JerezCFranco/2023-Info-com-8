# -Crea una función llamada es_anagrama que tome dos cadenas de texto como
# parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
# letras pero en distinto orden), o False en caso contrario.
def esAnagrama(texto1,texto2):
    if (sorted(texto1)==sorted(texto2)):
        return ("Las palabras ingresadas son Anagrama.")
    else:
        return ("Las palabras ingresadas no son Anagrama.")

print("Bienvenido, se le solicitara ingresar dos palabras para analizar si son Anagrama.")
texto1=input("Escriba la primer palabra: ")
texto1=texto1.lower()
texto2=input("Escriba la segunda palabra: ")
texto2=texto2.lower()
print(esAnagrama(texto1,texto2))