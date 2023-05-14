#-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
#pantalla si está aprobado (5 o más) o no.

nota_alumno = int(input("Ingrese la nota del alumno: "))

if (nota_alumno>=5 and nota_alumno<11):
    print("El alumno esta aprobado.")
elif nota_alumno>10:
    print("Nota ingresada no valida.")
else:
    print("El alumno esta desaprobado.")