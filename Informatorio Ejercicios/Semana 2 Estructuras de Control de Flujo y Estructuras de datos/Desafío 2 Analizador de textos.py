#Ingrese un Texto o una frase

texto= input("Escriba un texto cualquiera, por ejemplo, un artículo o frase: ");
print("Ingrese tres letras a su elección: ");
texto= texto.lower();
letra1= input("Ingrese la primer letra: ");
letra1= letra1.lower();
letra2= input("Ingrese la segunda letra: ");
letra2= letra2.lower();
letra3= input("Ingrese la tercera letra: ");
letra3= letra3.lower();

cantidad_letra1 = texto.count(letra1);
cantidad_letra2 = texto.count(letra2);
cantidad_letra3 = texto.count(letra3);
numero_total_letras = len(texto);
print(f"La cantidad de veces que aparece {letra1}, es de {cantidad_letra1} veces.");
print(f"La cantidad de veces que aparece {letra2}, es de {cantidad_letra2} veces.");
print(f"La cantidad de veces que aparece {letra3}, es de {cantidad_letra3} veces.");
cadena_texto = texto.split();
print(f"La primera letra es: {cadena_texto[0][0]}, y la última es: {cadena_texto[-1][-1]}.");
print(f"El texto tiene en total : {numero_total_letras} letras, contando los espacios.");
texto_inverso = cadena_texto[:];
texto_inverso.reverse();
print(f"El texto al inverso es : {texto_inverso}.");
if ("python" in texto):
    print("La palabra python si aparece en el texto.");
else:
    print("La palabra python no aparece en el texto.");
