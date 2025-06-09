# archivo: main.py
from user import Usuario
from auth import registrar_usuario, iniciar_sesion, buscar_usuario
from menu import menu_usuario, menu_admin

# Lista que simula nuestra "base de datos"
usuarios = [
    Usuario("admin", "admin123", "admin"),  # Usuario inicial con rol admin
]

def mostrar_menu_principal():
    print("\n SISTEMA DE USUARIOS - E-commerce de Tecnología")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            usuario = iniciar_sesion(usuarios)
            if usuario:
                if usuario.rol == "admin":
                    menu_admin(usuarios)
                else:
                    menu_usuario(usuario)
        elif opcion == "3":
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    main()
