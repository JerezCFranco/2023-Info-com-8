#Escribe un programa que solicite al usuario dos números y luego imprima la
#suma, la resta, la multiplicación y la división de los dos números.

num1 = int(input("Escriba el primer número: "));
num2 = int(input("Escriba el segundo número: "));

suma = num1+num2;
resta = num1-num2;
multiplicación = num1*num2;
división = num1/num2;

print(F"La suma de los números es:{suma}, su resta es:{resta}, su multiplicación es:{multiplicación}, y su división es:{división}.");