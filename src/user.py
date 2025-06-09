# archivo: user.py
class Usuario:
    """
    Representa a un usuario del sistema.
    Atributos:
        - nombre_usuario: nombre de acceso
        - contraseña: clave de acceso (mín. 6 caracteres, debe tener letras y números)
        - rol: 'admin' o 'usuario'
    """
    def __init__(self, nombre_usuario, contrasenia, rol="usuario"):
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.rol = rol

    def mostrar_datos(self):
        return f"Usuario: {self.nombre_usuario} | Rol: {self.rol}"


