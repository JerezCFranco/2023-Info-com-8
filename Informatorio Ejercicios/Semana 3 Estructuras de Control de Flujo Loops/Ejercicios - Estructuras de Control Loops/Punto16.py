# -Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con cada palabra al revés.

texto = input("Ingrese un texto cualquiera: ")
texto_alreves= "".join(reversed(texto))
print(texto)
print(texto_alreves)


