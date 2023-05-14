# -Escribe un programa que pida al usuario una cadena de texto y luego imprima
# el número de palabras que contiene.
cadena=input("Escriba una cadena de texto: ")
cadena_lista = cadena.split(" ")
print(f"El texto contiene {len(cadena_lista)} palabras.")