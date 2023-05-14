#Escribe un programa que solicite al usuario su nombre y su edad, y luego
#imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

nombre = input("Ingrese su nombre: ");
edad = int(input("Ingrese su edad: "));
edad_en_10_años = edad+10;
print(F"En 10 años {nombre}, tendra {edad_en_10_años} años.");