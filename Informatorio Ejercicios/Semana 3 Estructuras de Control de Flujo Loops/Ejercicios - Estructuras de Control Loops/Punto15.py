# -Escribe un programa que pida al usuario una cadena de texto y determine
# cuántas veces aparece cada letra en la cadena.
palabra = input("Escriba unas palabras cualquiera: ")
palabra=palabra.lower()
letras_dic = dict() 
contador = 0 

for letra in palabra: 
    if letra in letras_dic: 
        if letras_dic[letra] == 1: 
            contador += 1 
        letras_dic[letra] += 1 
    else:
        letras_dic[letra] = 1 
print("Las cantidad de veces que se repite cada palabra de la cadena es: ")
print(letras_dic)
print("")

