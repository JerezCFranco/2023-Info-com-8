# -Crea una función llamada invertir_cadena que tome una cadena de texto como
# parámetro y devuelva la cadena invertida.

def cadenaInvertida(texto):
    cadena_texto=texto.split()
    cadena_inversa=cadena_texto[:]
    cadena_inversa.reverse()
    strcadena=" ".join(cadena_inversa)
    return(strcadena)

texto= input("Ingrese un texto o frase cualquiera: ")
print(cadenaInvertida(texto))