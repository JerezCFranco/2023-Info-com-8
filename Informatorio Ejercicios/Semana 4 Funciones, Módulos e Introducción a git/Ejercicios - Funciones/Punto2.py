# -Crea una función llamada saludo que tome el nombre de una persona como
# parámetro e imprima un saludo personalizado.

def saludo(nombre):
    return (f"¡Hola {nombre}! Bienvenido a este programa que prueba la funcionalidad de la función saludo.")

print("Se le pedira que escriba su nombre por pantalla.")
nombre= input("Escriba su nombre: ")
print(saludo(nombre))