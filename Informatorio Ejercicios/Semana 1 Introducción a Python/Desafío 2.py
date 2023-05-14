#Escribe un programa que solicite al usuario su información personal, incluyendo
#su nombre completo, edad, estatura, peso, dirección y número de teléfono.
#A continuación, el programa deberá imprimir un mensaje con los datos
#ingresados por el usuario en el siguiente formato:

nombre_completo = input("Ingrese su nombre completo: ");
edad = int(input("Ingrese su edad: "));
estatura = int(input("Ingrese su estatura en centimetros: "));
peso = int(input("Ingrese su peso en kilogramos: "));
dirección = input("Ingrese su dirección: ");
numero_de_telefono = int(input("Ingrese su número de teléfono: "));

print(F"Nombre completo: {nombre_completo}.");
print(F"Edad: {edad} años.");
print(F"Estatura: {estatura} cm.");
print(F"Peso: {peso} kg.");
print(F"Dirección: {dirección}.");
print(F"Número de teléfono: {numero_de_telefono}.");