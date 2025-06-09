# archivo: auth.py
import re
from user import Usuario

def validar_contrasenia(contrasenia):
    """
    Valida que la contraseña tenga mínimo 6 caracteres y contenga letras y números.
    """
    return (
        len(contrasenia) >= 6 and
        re.search(r"[A-Za-z]", contrasenia) and
        re.search(r"[0-9]", contrasenia)
    )

def buscar_usuario(nombre, lista_usuarios):
    """
    Busca un usuario por nombre en la lista de usuarios.
    """
    for usuario in lista_usuarios:
        if usuario.nombre_usuario == nombre:
            return usuario
    return None

def registrar_usuario(lista_usuarios):
    """
    Registra un nuevo usuario con validación de nombre único y contraseña.
    """
    nombre = input("Ingrese nombre de usuario: ")
    if buscar_usuario(nombre, lista_usuarios):
        print(" Ya existe un usuario con ese nombre.")
        return

    contrasenia = input("Ingrese contraseña (mín. 6 caracteres, letras y números): ")
    if not validar_contrasenia(contrasenia):
        print(" Contraseña inválida.")
        return

    nuevo_usuario = Usuario(nombre, contrasenia)
    lista_usuarios.append(nuevo_usuario)
    print(" Usuario registrado exitosamente.")

def iniciar_sesion(lista_usuarios):
    """
    Permite iniciar sesión. Retorna el objeto Usuario si las credenciales son válidas.
    """
    nombre = input("Usuario: ")
    contrasenia = input("Contraseña: ")
    usuario = buscar_usuario(nombre, lista_usuarios)
    if usuario and usuario.contrasenia == contrasenia:
        print(f"Bienvenido, {usuario.nombre_usuario} ({usuario.rol})")
        return usuario
    else:
        print(" Credenciales incorrectas.")
        return None

