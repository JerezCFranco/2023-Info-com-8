resultado = True
dato = int(input("Valor"))
divisor = 2

while ((divisor<dato) and resultado):
    if (dato%divisor==0):
        resultado=False

    divisor = divisor+1

if(resultado):
    print("Si,es!")
else:
    print("No,no es!")