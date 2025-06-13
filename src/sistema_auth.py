# sistema_auth.py
from user import Usuario
import re

class SistemaAuth:
    def __init__(self):
        # Atributo principal: la lista de usuarios registrados
        self.lista_usuarios = [
            Usuario("admin", "admin123", "admin")
        ]

    def validar_contrasenia(self, contrasenia):
        """
        Valida que la contraseña tenga al menos 6 caracteres,
        y que incluya letras y números.
        """
        return (
            len(contrasenia) >= 6 and
            re.search(r"[A-Za-z]", contrasenia) and
            re.search(r"[0-9]", contrasenia)
        )

    def buscar_usuario(self, nombre):
        """
        Busca un usuario por nombre en la lista.
        Retorna el objeto Usuario si lo encuentra.
        """
        for usuario in self.lista_usuarios:
            if usuario.nombre_usuario == nombre:
                return usuario
        return None

    def registrar_usuario(self):
        """
        Registra un nuevo usuario si no está repetido y la contraseña es válida.
        """
        nombre = input("Ingrese nombre de usuario: ")
        if self.buscar_usuario(nombre):
            print("Ya existe un usuario con ese nombre.")
            return

        contrasenia = input("Ingrese contraseña: ")
        if not self.validar_contrasenia(contrasenia):
            print("Contraseña inválida.")
            return

        nuevo_usuario = Usuario(nombre, contrasenia)
        self.lista_usuarios.append(nuevo_usuario)
        print("Usuario registrado exitosamente.")

    def iniciar_sesion(self):
        """
        Permite iniciar sesión si el nombre y contraseña coinciden.
        Retorna el objeto Usuario si es válido.
        """
        nombre = input("Usuario: ")
        contrasenia = input("Contraseña: ")
        usuario = self.buscar_usuario(nombre)
        if usuario and usuario.contrasenia == contrasenia:
            print(f"Bienvenido, {usuario.nombre_usuario} ({usuario.rol})")
            return usuario
        print("Credenciales incorrectas.")
        return None
