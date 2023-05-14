#Ingrese dos numeros enteros, obtendremos la suma, el cociente y el resto de estos.

num1= float(input("Ingrese el primer numero: "));
num2= float(input("Ingrese el segundo numero: "));

suma = num1+num2;
cociente = int(num1/num2);
resto = num1-(cociente*num2);

print(F"La suma de los números es: {suma}.");
print(F"El cociente de los números es: {cociente}.");
print(F"El resto de los números es: {resto}.");
