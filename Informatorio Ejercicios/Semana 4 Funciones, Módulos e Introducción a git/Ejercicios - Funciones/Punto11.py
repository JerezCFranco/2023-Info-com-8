# -Crea una función llamada contar_vocales que tome una cadena de texto como
# parámetro y devuelva el número de vocales que contiene.

def contar_vocales(cad):
    voc = 0
    for c in cad:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            voc=voc+1
    return (f"La cantidad de vocales en el texto es de : {voc}")


cad = input("Escriba un texto cualquiera: ")
print(contar_vocales(cad))