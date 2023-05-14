#Escribir un programa que pida al usuario una letra y muestre por pantalla si es
#una vocal o una consonante.

letra = input("Ingrese una letra: ")
letra= letra.lower()
numeros = ["1","2","3","4","5","6","7","8","9"]
caracter_especial = ["|","!","@","#","$","%","&","/","()","=","?","¡","{","}","+","-","*"]
vocal = ["a","e","i","o","u"]
consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","z"]
if letra in vocal:
    print("La letra ingresada es una vocal.")
elif letra in numeros:
    print("Error, no ingreso una letra, ingreso un número.")
elif letra in caracter_especial:
    print("Error, no ingreso una letra, ingreso un carácter especial.")
elif letra in consonantes:
    print("La letra ingresada es una consonante.")
else:
    print("Error, la letra ingresada es invalida.")