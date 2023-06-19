# Ejercicio 3: Triángulo
# Desarrollar un programa que cargue los datos de un triángulo.
# Implementar una clase con los métodos para inicializar los atributos, imprimir el
# valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
# isósceles o escaleno).

class triángulo:
    def __init__(self, angulo1, angulo2, angulo3):
        self.angulo1=angulo1
        self.angulo2=angulo2
        self.angulo3=angulo3

    def comparar_angulos(self):
        if (self.angulo1 > self.angulo2 and self.angulo1 > self.angulo3 and self.angulo2 > self.angulo3):
            return (f"El triángulo es escaleno, su mayor lado es el de {self.angulo1} grados, seguido del angulo de {self.angulo2} grados, y su angulo mas pequeño es el {self.angulo3} grados.")
        elif(self.angulo1 > self.angulo2 and self.angulo1 > self.angulo3 and self.angulo3 > self.angulo2):
            return (f"El triángulo es escaleno, su mayor lado es el de {self.angulo1} grados, seguido del angulo de {self.angulo3} grados, y su angulo mas pequeño es el {self.angulo2} grados.")
        elif(self.angulo2 > self.angulo1 and self.angulo2 > self.angulo3 and self.angulo1 > self.angulo3):
            return (f"El triángulo es escaleno, su mayor lado es el de {self.angulo2} grados, seguido del angulo de {self.angulo1} grados, y su angulo mas pequeño es el {self.angulo3} grados.")
        elif(self.angulo2 > self.angulo1 and self.angulo2 > self.angulo3 and self.angulo3 > self.angulo1):
            return (f"El triángulo es escaleno, su mayor lado es el de {self.angulo2} grados, seguido del angulo de {self.angulo3} grados, y su angulo mas pequeño es el {self.angulo1} grados.")
        elif(self.angulo3 > self.angulo1 and self.angulo3 > self.angulo2 and self.angulo1 > self.angulo2):
            return (f"El triángulo es escaleno, su mayor lado es el de {self.angulo3} grados, seguido del angulo de {self.angulo1} grados, y su angulo mas pequeño es el {self.angulo2} grados.")
        elif(self.angulo3 > self.angulo1 and self.angulo3 > self.angulo2 and self.angulo2 > self.angulo1):
            return (f"El triángulo es escaleno, su mayor lado es el de{self.angulo3} grados, seguido del angulo de {self.angulo2} grados, y su angulo mas pequeño es el {self.angulo1} grados.")
        elif(self.angulo1 == self.angulo2 and self.angulo1 > self.angulo3):
            return (f"El triángulo es isóceles, sus lados iguales son de {self.angulo1} grados, y el lado de menor es de {self.angulo3} grados.")
        elif(self.angulo1 == self.angulo3 and self.angulo1 > self.angulo2):
            return (f"El triángulo es isóceles, sus lados iguales son de {self.angulo1} grados, y el lado de menor es de {self.angulo2} grados.")
        elif(self.angulo2 == self.angulo3 and self.angulo2 > self.angulo1):
            return (f"El triángulo es isóceles, sus lados iguales son de {self.angulo2} grados, y el lado de menor es de {self.angulo1} grados.")
        elif(self.angulo1 == self.angulo2 and self.angulo1 == self.angulo3):
            return (f"El triángulo es equilátero, todos sus lados son de {self.angulo1} grados.")
        else:
            return("Error, datos invalidos.")
        
triángulo1= triángulo(80, 75, 90)

print(triángulo1.comparar_angulos())