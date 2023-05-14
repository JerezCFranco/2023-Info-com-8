#Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
#e imprima su índice de masa corporal (IMC).
#La fórmula para calcular el IMC es: IMC = peso / (altura ** 2)

peso = int(input("Ingrese su peso en kg: "));
altura = float(input("Ingrese su altura en m: "));
masa_corporal = peso/(altura*altura);

print(F"Un sujeto con un peso de {peso} kg, y una altura de {altura} cm, la masa corporal del sujeto es de : {masa_corporal}.");
