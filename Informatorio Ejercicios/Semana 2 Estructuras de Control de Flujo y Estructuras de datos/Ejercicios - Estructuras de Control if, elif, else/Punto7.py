#Escribir un programa que pida al usuario un carácter y muestre por pantalla si
#es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input("Ingrese un carácter cualquiera: ")
numeros = ["1","2","3","4","5","6","7","8","9"]
caracter_especial = ["|","!","@","#","$","%","&","/","()","=","?","¡","{","}","+","-","*"]
if caracter in caracter_especial:
    print("El carácter introducido es un carácter especial.")
elif caracter in numeros:
    print("El carácter introducido es un número.")
elif (caracter == caracter.upper()):
    print("El carácter introducido es una letra mayúscula.")
elif (caracter == caracter.lower()):
    print("El carácter introducido es una letra minúscula.")
else:
    print("error.")
