--✅ CREATE (Insertar nuevo usuario)

INSERT INTO usuarios (nombre_usuario, contraseña, rol)
VALUES ('juan23', 'clave123', 'usuario');

--✅ READ (Consultar usuarios)
a. Todos los usuarios
SELECT * FROM usuarios;


 Un usuario específico
SELECT * FROM usuarios
WHERE nombre_usuario = 'juan23';


--✅ UPDATE (Modificar contraseña o rol)
UPDATE usuarios
SET contraseña = 'nuevaClave456', rol = 'admin'
WHERE nombre_usuario = 'juan23';


--✅ DELETE (Eliminar usuario)
DELETE FROM usuarios
WHERE nombre_usuario = 'juan23';
