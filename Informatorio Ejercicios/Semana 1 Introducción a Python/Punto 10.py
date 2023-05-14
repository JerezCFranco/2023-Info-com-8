#Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros.
#Supón que el tipo de cambio es de 0.84 euros por dólar.

euro= 0.84;
cantidad_dolares = int(input("Ingrese la cantidad de dólares: "));
dolares_a_euros=cantidad_dolares*euro;

print(F"Con {cantidad_dolares} dólares, se obtienen {dolares_a_euros} euros.");
