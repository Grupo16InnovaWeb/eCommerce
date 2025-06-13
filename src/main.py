# main.py
from sistema_auth import SistemaAuth
from menu_sistema import MenuSistema

def mostrar_menu_principal():
    print("\nSISTEMA DE USUARIOS - E-commerce de Tecnología")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

def main():
    auth = SistemaAuth()
    menu = MenuSistema()

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            auth.registrar_usuario()
        elif opcion == "2":
            usuario = auth.iniciar_sesion()
            if usuario:
                if usuario.rol == "admin":
                    menu.mostrar_menu_admin(auth)
                else:
                    menu.mostrar_menu_usuario(usuario)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
