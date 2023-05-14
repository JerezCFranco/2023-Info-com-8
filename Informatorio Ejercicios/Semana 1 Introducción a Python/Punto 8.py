#Crea un programa que pida al usuario el radio de un círculo y muestre su
#diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159.

pi = 3.14159;
radio = int(input("Escriba el radio del círculo: "));
diámetro = radio*2;
circunferencia = 2*pi*radio;
área = pi*(radio*radio);

print(F"El diámetro del círculo es {diámetro}.");
print(F"La circunferencia del círculo es {circunferencia}.");
print(F"El área del círculo es {área}.");