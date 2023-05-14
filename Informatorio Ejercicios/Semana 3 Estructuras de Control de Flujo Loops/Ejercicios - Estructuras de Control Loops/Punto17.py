# -Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con las palabras en orden inverso.
texto= input("Ingrese un texto o frase cualquiera: ")
cadena_texto=texto.split()
cadena_inversa=cadena_texto[:]
cadena_inversa.reverse()
strcadena=" ".join(cadena_inversa)
print(strcadena)
