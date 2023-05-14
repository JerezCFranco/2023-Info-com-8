#-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es múltiplo de 2 y de 3 a la vez.

numero = int(input("Ingrese un número cualquiera: "))

if ((numero%2 == 0) and (numero%3 ==0)):
    print("El número es múltiplo de 2 y de 3 a la vez.")
elif (numero%2==0):
    print("El número es solo múltiplo de 2.")
elif (numero%3==0):
    print("El número es solo múltiplo de 3.")
else:
    print("El número no es multiplo ni de 2 ni de 3.")