SHOW DATABASES; -- Mostrar las bases de datos

CREATE DATABASE mer_tablas; -- Crea una base de datos llamada mer_tablas

USE mer_tablas; -- Acceder a la base de datos mer_tablas

SHOW TABLES; -- Mostrar las tablas.

CREATE TABLE blog(
    nombre CHAR(20)
    url CHAR(255)
    PRIMARY KEY (nombre)
);