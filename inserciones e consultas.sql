USE finca;


Insert into Usuario(ID, Nombre, Apellido, Cedula) values  
(1, 'alfredo', 'zanches', 1109843602),
(4, 'alcatraz', 'figueroa', 1109843603),
(3, 'sisiyua', 'zanches', 1109843604);

INSERT into Ganado   (ID, Especie, Tamaño) values
(1, 'ovino', 'mediano'),
(2, 'porcino', 'grande'),
(3, 'equino', 'extra grander');

Insert into Comprador   (ID, Nombre, Apellido, Cedula,Ganado_ID) values  
(1, 'alex', 'gonzalez', 1340187352, 1),
(2, 'fredy', 'roa', 1234235481, 3),
(3, 'diego', 'perez', 1109842499,2),
(4, 'dibu', 'leo', 1109842499,1);
insert into ventas (ID, Cantidad, Especie, Usuario_ID, Ganado_ID) values 
(1, 3, 'brahman', 4, 2),
(2, 5, 'holstein', 4, 3),
(3, 10, 'jersey', 3, 1);


SELECT ID, Nombre FROM Usuario;
SELECT Cantidad FROM ventas;
select especie from ventas;
SELECT ID, Especie FROM Ganado;
select usuario.nombre, ganado,especie. ganado.tamaño from Usuarios inner join ganado on usuarios.id_usuario = ganado.id_usuario;
SELECT ID, Nombre FROM Usuario WHERE Cedula = 123456789;
