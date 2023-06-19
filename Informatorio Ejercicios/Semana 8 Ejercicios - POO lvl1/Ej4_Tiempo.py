# Ejercicio 4: Tiempo
# Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
# instanciada indicando: los tres atributos, sólo la hora y minuto, o sólo la hora.
# Crear además los métodos necesarios para modificar la hora en cualquier
# momento de forma manual. Mantenga la integridad de los datos en todo
# momento definiendo de tipo “private”. Crear una clase prueba_tiempo que
# prueba una hora concreta y la modifique a su gusto mostrándola por pantalla.

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, teléfono, username, email, contraseña, fecha_de_registro, avatar, estado, online):
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.apellido=apellido
        self.teléfono=teléfono
        self.username=username
        self.email=email
        self.contraseña=contraseña
        self.fecha_de_registro=fecha_de_registro
        self.avatar=avatar
        self.estado=estado
        self.online=online

    def login(self):
        k=0
        nombre=input("Ingrese su usuario: ")
        contraseña=input("Ingrese su contraseña: ")
        for x in range(len(usuarios_registrados)):
            if (usuarios_registrados[x].username==nombre and usuarios_registrados[x].contraseña==contraseña):
                print(f"\n Bienvenido denuevo {usuarios_registrados[x].username}. \n")
                print(verplantilla())
                return("")
            else:
                print("El usuario o contraseña ingresados son incorrectos, intente nuevamente.")
                return""
    
    def registrar(self):
        id_usuario=usuarios_registrados[-1].id_usuario+1
        nombre=input("Ingrese su nombre: ")
        apellido=input("Ingrese su apellido: ")
        teléfono=int(input("Ingrese su número de teléfono: "))
        username=input("Ingrese el nombre de usuario que utilizara: ")
        email=input("Ingrese su dirección de email: ")
        fecha_de_registro=input("Ingrese la fecha actual(en formato dd/mm/aaaa): ")
        avatar=input("Ingrese el link de su avatar: ")
        estado="Activo"
        online="En linea"
        datox=""
        if (usuarios_registrados[-1].id_usuario+1==3):
            us3=Usuario(id_usuario, nombre, apellido, teléfono, username, email, fecha_de_registro, avatar, estado, online,datox)
            usuarios_registrados.append(us3)
            return""
        elif (usuarios_registrados[-1].id_usuario+1==4):
            us4=Usuario(id_usuario, nombre, apellido, teléfono, username, email, fecha_de_registro, avatar, estado, online)
            usuarios_registrados.append(us4)
            return""
        elif (usuarios_registrados[-1].id_usuario+1==5):
            us5=Usuario(id_usuario, nombre, apellido, teléfono, username, email, fecha_de_registro, avatar, estado, online)
            usuarios_registrados.append(us5)
            return""
        elif (usuarios_registrados[-1].id_usuario+1==6):
            us6=Usuario(id_usuario, nombre, apellido, teléfono, username, email, fecha_de_registro, avatar, estado, online)
            usuarios_registrados.append(us6)
            return""
        elif (usuarios_registrados[-1].id_usuario+1==7):
            us7=Usuario(id_usuario, nombre, apellido, teléfono, username, email, fecha_de_registro, avatar, estado, online)
            usuarios_registrados.append(us7)
            return""
        elif (usuarios_registrados[-1].id_usuario+1==8):
            us8=Usuario(id_usuario, nombre, apellido, teléfono, username, email, fecha_de_registro, avatar, estado, online)
            usuarios_registrados.append(us8)
            return""
        elif (usuarios_registrados[-1].id_usuario+1==9):
            us9=Usuario(id_usuario, nombre, apellido, teléfono, username, email, fecha_de_registro, avatar, estado, online)
            usuarios_registrados.append(us9)
            return""
        elif (usuarios_registrados[-1].id_usuario+1==10):
            us10=Usuario(id_usuario, nombre, apellido, teléfono, username, email, fecha_de_registro, avatar, estado, online)
            usuarios_registrados.append(us10)
            return""
        else:
            return ("Error al registrarse.")

class Publico(Usuario):
    def __init__(self, id_usuario, nombre, apellido, teléfono, username, email, contraseña, fecha_de_registro, avatar, estado, online, es_publico):
        super().__init__(id_usuario, nombre, apellido, teléfono, username, email, contraseña, fecha_de_registro, avatar, estado, online)
        self.es_publico=es_publico

    def comentar(self):
        print(escribir_comentario())



class Colaborador(Usuario):
    def __init__(self, id_usuario, nombre, apellido, teléfono, username, email, contraseña, fecha_de_registro, avatar, estado, online, es_colaborador):
        super().__init__(id_usuario, nombre, apellido, teléfono, username, email, contraseña, fecha_de_registro, avatar, estado, online)
        self.es_colaborador=es_colaborador

    def comentar(self):
        print(escribir_comentario())
    
    def publicar(self):
        id_articulo=usuarios_registrados[-1].id_usuario+1
        id_usuario=usuarios_registrados[-1].id_usuario+1
        titulo=input("Ingrese el titulo del articulo: ")
        resumen=input("Ingrese un resumen del articulo: ")
        contenido=input("Ingrese el contenido completo del articulo: ")
        fecha_publicacion=input("Ingrese la fecha actual(en formato dd/mm/aaaa): ")
        imagen=input("Ingrese el link de la imagen que usara el articulo: ")
        estado="En linea"
        if (usuarios_registrados[-1].id_usuario+1==3):
            art3=Articulo(id_articulo, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado)
            art3.titulo=titulo
            articulos.append(titulo)
            id_articulo=usuarios_registrados[-1].id_usuario+1
            articulo_n.append(id_articulo)
            comentarios.append("")
            return""



class Articulo:
    def __init__(self, id_articulo, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id_articulo=id_articulo
        self.id_usuario=id_usuario
        self.titulo=titulo
        self.resumen=resumen
        self.contenido=contenido
        self.fecha_publicacion=fecha_publicacion
        self.imagen=imagen
        self.estado=estado


articulo_n=[1,2,3]
articulos=["Flores","Edificio","Futbol"]
comentarios=["Que bellas flores!!","Wow, que gran edificio","Te queremos Messi",]

class Comentario:
    def __init__(self, id_comentario, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id_comentario=id_comentario
        self.id_articulo=id_articulo
        self.id_usuario=id_usuario
        self.contenido=contenido
        self.fecha_hora=fecha_hora
        self.estado=estado



def escribir_comentario():
    n=int(input("Indique el articulo que quiere comentar: "))
    if n==1:
        com=input("Escriba su comentario: ")
        comentarios[0]=comentarios[0]+" | "+com
    elif n==2:
        com=input("Escriba su comentario: ")
        comentarios[1]=comentarios[1]+" | "+com
    elif n==3:
        com=input("Escriba su comentario: ")
        comentarios[2]=comentarios[2]+" | "+com
    elif n==4:
        com=input("Escriba su comentario: ")
        comentarios[3]=comentarios[3]+" | "+com
    else:
        print("error")



def verplantilla():
    print("   Articulos  |     Comentarios ")
    for x in range(len(articulos)):
        print("   ",articulos[x],"      ",comentarios[x])
    return ""

def plantilla_colaborador():
    print("  Menú Colaborador: \n 1- Comentar Articulo \n 2- Publicar Articulo \n 0- Desconectarse ")
    eleccion=int(input("Ingrese su elección: "))
    if eleccion==1:
        print(colaborador1.comentar())
    elif eleccion==2:
        print(colaborador1.publicar())
    elif eleccion==0:
        print(verplantilla())
    else:
        print("Dato ingresado invalido, intente nuevamente.")

def plantilla_publico():
    print("  Menú: \n 1- Comentar Articulo \n 0- Desconectarse ")
    eleccion=int(input("Ingrese su elección: "))
    if eleccion==1:
        print(publico1.comentar())
    elif eleccion==0:
        print(verplantilla())

us1=Colaborador(1,"carlitos","jerez",3644,"carlitos","gmail","carlitos1","fecha","avatar","estado","online","si")
us2=Colaborador(2,"usuario2","apellido2",3634,"username2","gmail2","contraseña2","fecha2","avatar2","estado2","online2",True)


usuarios_registrados=[us1,us2]


publico1=Publico(1,"carlos","jerez",3644,"carlitos","gmail","carlitos1","15/06/23","avatar",True,True,True)

#def __init__(self, id_usuario, nombre, apellido, teléfono, username, email, contraseña, fecha_de_registro, avatar, estado, online, es_colaborador):

colaborador1=Colaborador(1,"seba","martinez",35445,"sebitas","gmailsebas","seba1","1/2/13","asd","activo","En linea","Es colaborador")

articulo1=Articulo(2,1,"titulo","resumen","contenido","fecha","imagen","estado")

print(usuarios_registrados[-1].id_usuario+1)

# print(publico1.registrar())


# print(publico1.comentar())

# print(verplantilla())

menu= int(input("Menú Principal: \n 1-Login \n 2-Registrarse \n 0-Salir \n -Ingrese su elección: "))
while menu !=0:
    if (menu==1):
        if (publico1.login()):
            print(verplantilla())
            if (colaborador1.es_colaborador=="si"):
                print(plantilla_colaborador())
            else:
                print(plantilla_publico())          
    elif(menu==2):
        print("")
    else:
        print ("Dato ingresado invalido, Intente nuevamente.")
    menu= int(input("Menú Principal: \n 1-Login \n 2-Registrarse \n 0-Salir \n -Ingrease su elección: "))
    