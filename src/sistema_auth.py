# sistema_auth.py
from user import Usuario
import re

class SistemaAuth:
    def __init__(self):
        self.lista_usuarios = [
            Usuario("admin", "admin123", "admin")
        ]

    def validar_contrasenia(self, contrasenia):
        return (
            len(contrasenia) >= 6 and
            re.search(r"[A-Za-z]", contrasenia) and
            re.search(r"[0-9]", contrasenia)
        )

    def buscar_usuario(self, nombre):
        for usuario in self.lista_usuarios:
            if usuario.nombre_usuario == nombre:
                return usuario
        return None

    def registrar_usuario(self):
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
        nombre = input("Usuario: ")
        contrasenia = input("Contraseña: ")
        usuario = self.buscar_usuario(nombre)
        if usuario and usuario.contrasenia == contrasenia:
            print(f"Bienvenido, {usuario.nombre_usuario} ({usuario.rol})")
            return usuario
        print("Credenciales incorrectas.")
        return None

