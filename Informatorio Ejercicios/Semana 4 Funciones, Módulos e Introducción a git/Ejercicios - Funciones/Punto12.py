# -Crea una función llamada convertir_temperatura que tome una temperatura
# en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
# es: Fahrenheit = (Celsius * 9/5) + 32.

def convertirTemperatura(temp):
    tempF= (temp*9/5)+32
    return tempF

temp=int(input("Ingresar la temperatura en grados Celsius: "))
print(f"La temperatura es de {convertirTemperatura(temp)}° Fahrenheit.")
    
