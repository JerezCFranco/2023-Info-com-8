-- Active: 1686176480629@@127.0.0.1@3306@desafio_7
CREATE DATABASE Blog;

USE Blog;

CREATE TABLE Usuario(
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    telefono INT,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_creación DATE,
    avatar VARCHAR(30) NOT NULL,
    es_publico BOOLEAN NOT NULL,
    es_colaborador BOOLEAN NOT NULL,
    es_admin BOOLEAN NOT NULL,
    PRIMARY KEY(id_usuario));

CREATE TABLE Articulo(
    id_articulo INT NOT NULL AUTO_INCREMENT,
    idusuario INT(20) NOT NULL,
    título VARCHAR(30) NOT NULL,
    resumen TEXT NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATE,
    estado BOOLEAN NOT NULL,
    imagen VARCHAR(100) NOT NULL,
    PRIMARY KEY(id_articulo),
    FOREIGN KEY(idusuario) REFERENCES Usuario(id_usuario));

CREATE TABLE Comentario(
    id_comentario INT NOT NULL AUTO_INCREMENT,
    idarticulo INT(20) NOT NULL,
    idusuario INT(20) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_hora DATETIME,
    estado BOOLEAN NOT NULL,
    PRIMARY KEY(id_comentario),
    FOREIGN KEY(idarticulo) REFERENCES Articulo(id_articulo),
    FOREIGN KEY(idusuario) REFERENCES Usuario(id_usuario));

CREATE TABLE Categoria(
    id_categoria INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    descripcion TEXT NOT NULL,
    imagen VARCHAR(100) NOT NULL,
    estado BOOLEAN NOT NULL,
    PRIMARY KEY(id_categoria));

CREATE TABLE Categoria_Articulo(
    idcategoria INT(20) NOT NULL,
    idarticulo INT(20) NOT NULL,
    FOREIGN KEY(idcategoria) REFERENCES Categoria(id_categoria),
    FOREIGN KEY(idarticulo) REFERENCES Articulo(id_articulo));

-- - Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol
-- de admin, 4 con rol de colaborador y 5 con rol de público. Donde los campos:
-- es_publico, es_colaborador y es_admin son booleanos.

-- -Comando para introducir a un usuario administrador
INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("José","Acosta", "elmascapito", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", FALSE, FALSE, TRUE);

-- -Comando para introducir 4 usuarios colaboradores

INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Enrique","Silva","enriquesilva", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", FALSE, TRUE, FALSE);
INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Colaborador N°2","Apellido2", "contraseña2", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", FALSE, TRUE, FALSE);
INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Colaborador N°3","Apellido3", "contraseña3", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", FALSE, TRUE, FALSE);
INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Colaborador N°4","Apellido4", "contraseña4", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", FALSE, TRUE, FALSE);

-- -Comando para introducir 5 usuarios publicos

INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Usuario Publico N°1","Apellido1", "contraseña1", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", TRUE, FALSE, FALSE);
INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Usuario Publico N°2","Apellido2", "contraseña2", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", TRUE, FALSE, FALSE);
INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Usuario Publico N°3","Apellido3", "contraseña3", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", TRUE, FALSE, FALSE);
INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Usuario Publico N°4","Apellido4", "contraseña4", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", TRUE, FALSE, FALSE);
INSERT INTO USUARIO(nombre, apellido, username, email, contraseña, estado, avatar, es_publico, es_colaborador, es_admin) VALUES ("Usuario Publico N°5","Apellido5", "contraseña5", "correo@gmail.com","123456", TRUE, "http://linkalavatar.com", TRUE, FALSE, FALSE);


-- - Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios
-- agregado con rol de colaborador.

UPDATE Usuario SET es_colaborador=FALSE, es_admin=TRUE WHERE id_usuario=2;

-- - Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con
-- estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es
-- Booleano.

-- -Comando para introducir 3 articulos con True
INSERT INTO Articulo(idusuario, título, resumen, contenido, estado, imagen) VALUES (1, "Título del articulo", "Resumen del articulo", "Contenido del articulo",TRUE,"http://link-imagen.com");
INSERT INTO Articulo(idusuario, título, resumen, contenido, estado, imagen) VALUES (2, "Título del articulo", "Resumen del articulo", "Contenido del articulo",TRUE,"http://link-imagen.com");
INSERT INTO Articulo(idusuario, título, resumen, contenido, estado, imagen) VALUES (3, "Título del articulo", "Resumen del articulo", "Contenido del articulo",TRUE,"http://link-imagen.com");

-- -Comando para introducir un articulo con False
INSERT INTO Articulo(idusuario, título, resumen, contenido, estado, imagen) VALUES (4, "Título del articulo", "Resumen del articulo", "Contenido del articulo",FALSE,"http://link-imagen.com");

-- - Agregar el comando necesario para eliminar el artículo que tenga estado FALSE.
DELETE FROM Articulo WHERE estado=FALSE;


-- - Agregar el comando necesario que introduzca 3 comentarios al primer artículo
-- agregado y 2 comentarios al segundo artículo.

-- -Comando para introducir 3 comentarios en el primer articulo
INSERT INTO Comentario(idusuario, idarticulo, contenido, estado)  VALUES (1, 1, "Comentario en el primer articulo", TRUE);
INSERT INTO Comentario(idusuario, idarticulo, contenido, estado)  VALUES (4, 1, "Comentario en el primer articulo", TRUE);
INSERT INTO Comentario(idusuario, idarticulo, contenido, estado)  VALUES (3, 1, "Comentario en el primer articulo", TRUE);

-- -Comando para introducir 2 comentarios en el seguno articulo
INSERT INTO Comentario(idusuario, idarticulo, contenido, estado)  VALUES (2, 2, "Comentario en el segundo articulo", TRUE);
INSERT INTO Comentario(idusuario, idarticulo, contenido, estado)  VALUES (5, 2, "Comentario en el segundo articulo", TRUE);


-- - Agregar el comando necesario para listar todos los artículos que tengan
-- comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
-- nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho
-- comentario, agrupados por artículos.
SELECT Articulo.título, Articulo.fecha_publicacion, Usuario.nombre AS nombre_usuario, Comentario.fecha_hora AS fecha_hora_comentario
FROM Articulo INNER JOIN Comentario ON Articulo.id_articulo = Comentario.idarticulo INNER JOIN Usuario ON Comentario.idusuario = Usuario.id_usuario
GROUP BY Articulo.id_articulo, Articulo.título, Articulo.fecha_publicacion, Usuario.nombre, Comentario.fecha_hora;