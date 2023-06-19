# Ejercicio 1: Vehículo pt.1
# A partir del siguiente diagrama de clases, implementá
# clases y métodos para mostrar atributos.


class vehículo:
    def __init__(self, nombre, color, ruedas, cantidad_ruedas):
        self.nombre="Vehículo"
        self.color="Azul"
        self.ruedas="Acero Forjado"
        self.cantidad_ruedas=4
    
    def caracteristicas_vehiculo(self):
        return(f"El vehículo tiene un color {self.color}, y unas ruedas de {self.ruedas}.")
    

class coche(vehículo):
    def __init__(self,nombre, color, ruedas, cantidad_ruedas, velocidad, cilindrada):
        super().__init__(nombre, color, ruedas, cantidad_ruedas)
        self.velocidad="200 km/h"
        self.cilindrada="1600 cc"

    def caracteristicas_coche(self):
        return(f"El coche tiene un color {self.color}, unas ruedas de {self.ruedas}, tiene una velocidad de {self.velocidad} km/h, y unas cilindradas de {self.cilindrada} cc.")

vehículo1=vehículo("Vehículo","Azul", "Acero Forjado",4)
print(vehículo1.caracteristicas_vehiculo())

coche1=coche("Coche","Azul", "Acero Forjado", 4, 200, 1600)
print(coche1.caracteristicas_coche())

class bicicleta:
    def __init__(self, nombre, tipo, cantidad_ruedas):
        self.nombre=nombre
        self.tipo=tipo
        self.cantidad_ruedas=cantidad_ruedas
    def caracteristica_bicicleta(self):
        return(f"La bicicleta es de tipo {self.tipo}.")

bicicleta1=bicicleta("Bicicleta", "Deportiva", 2)


class motocicleta:
    def __init__(self,nombre, velocidad, cilindrada, cantidad_ruedas):
        self.nombre=nombre
        self.velocidad=velocidad
        self.cilindrada=cilindrada
        self.cantidad_ruedas=cantidad_ruedas
    
    def caracteristicas_motocicleta(self):
        return(f"La moto llega a velocidades de {self.velocidad} km/h, y tiene una cialindrada {self.cilindrada} cc.")

motocicleta1=motocicleta("Motocicleta", 120, 150, 2)


class camioneta:
    def __init__(self,nombre, carga, cantidad_ruedas):
        self.nombre=nombre
        self.carga=carga
        self.cantidad_ruedas=cantidad_ruedas
    
    def caracteristicas_camioneta(self):
        return(f"La camioneta tiene una carga de {self.carga} km.")

camioneta1=camioneta("Camioneta",1000, 6)

vehículos = [vehículo1.caracteristicas_vehiculo(),coche1.caracteristicas_coche(), bicicleta1.caracteristica_bicicleta(), motocicleta1.caracteristicas_motocicleta(),camioneta1.caracteristicas_camioneta()]

vehículos1= [vehículo1,coche1,bicicleta1,motocicleta1,camioneta1]

def catalogar():
    x = 0
    while x < len(vehículos):
        return(vehículos)
        x+=1

def catalogar_ruedas():
    cantidad_analizar = int(input("Ingrese la cantidad de ruedas a analizar de los vehículos: "))
    x = 0
    while x < len(vehículos1):
        if(vehículos1[x].cantidad_ruedas==cantidad_analizar):
            print(f"El/La {vehículos1[x].nombre} tiene {vehículos1[x].cantidad_ruedas} ruedas.")
        else:
            print(f"El/La {vehículos1[x].nombre} no tiene {cantidad_analizar} ruedas.")
        x+=1
    return ""

print(catalogar_ruedas())




    