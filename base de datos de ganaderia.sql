DROP DATABASE IF EXISTS finca;
CREATE DATABASE IF NOT EXISTS finca;
USE finca;

CREATE TABLE Usuario(
ID int primary key not null,
Nombre varchar (50) not null,
Apellido varchar (50) not null,
Cedula int not null);

CREATE TABLE Ganado(
ID int primary key not null, 
Especie varchar (50) not null,
Tamaño varchar (50) not null);

CREATE TABLE Comprador(
ID int primary key not null, 
Nombre varchar (50) not null,
Apellido varchar (50) not null,
Cedula int not null,
Ganado_ID int not null, 
foreign key (Ganado_ID) REFERENCES Ganado(ID)
);

CREATE TABLE ventas(
ID int primary key not null,
Cantidad int not null, 
Especie varchar (50) not null,
Usuario_ID int not null,
Ganado_ID int not null,
foreign key (Usuario_ID) REFERENCES Usuario(ID),
FOREIGN KEY (Ganado_ID) REFERENCES Ganado(ID)
);

