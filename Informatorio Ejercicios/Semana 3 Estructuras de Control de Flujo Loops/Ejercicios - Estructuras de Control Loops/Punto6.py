# -Escribe un programa que pida al usuario una palabra y luego imprima la misma
# palabra pero con las letras en orden inverso.
texto = input("Escribir una palabra: ")
palabras = texto.split()
for palabra in palabras:
    print(palabra[::-1], end = ' ')
