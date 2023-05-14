# -Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.
x=0
y=1
z=0
while True:
    numero=int(input("Ingrese un número, debe ser mayor a 1: "))
    if numero>1:
        break
print ("1", end=" ")
for i in range(0,numero):
    z=x+y
    print(f"{z}",end=" ")
    x=y
    y=z
print("")