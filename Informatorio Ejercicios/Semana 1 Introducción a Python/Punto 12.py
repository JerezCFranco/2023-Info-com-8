#Escribe un programa que solicite al usuario su fecha de nacimiento en formato
#dd/mm/aaaa y luego imprima su edad en años.
#Utiliza la función .split()

año_actual = int(input("Ingrese el año actual: "));
fecha_de_nacimiento = [];
dia_nacimiento = int(input("Ingrese el día de su nacimiento: "));
mes_nacimiento = int(input("Ingrese el mes de nacimiento: "));
año_nacimiento = int(input("Ingrese su año de nacimiento: "));

fecha_de_nacimiento.append(dia_nacimiento);
fecha_de_nacimiento.append(mes_nacimiento);
fecha_de_nacimiento.append(año_nacimiento);

edad= año_actual-año_nacimiento;

print(F"La edad del usuario es de: {edad}.");
