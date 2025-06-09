from auth import buscar_usuario


# archivo: menu.py
def menu_usuario(usuario):
    """
    Menú para el usuario estándar. Solo puede ver sus datos.
    """
    print("\n MENÚ DE USUARIO")
    print(usuario.mostrar_datos())

def menu_admin(lista_usuarios):
    """
    Menú para el administrador. Puede ver, modificar y eliminar usuarios.
    """
    while True:
        print("\n MENÚ ADMINISTRADOR")
        print("1. Ver usuarios")
        print("2. Cambiar rol")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            for u in lista_usuarios:
                print(u.mostrar_datos())
        elif opcion == "2":
            nombre = input("Ingrese usuario a modificar: ")
            usuario = buscar_usuario(nombre, lista_usuarios)
            if usuario:
                nuevo_rol = input("Nuevo rol (admin/usuario): ")
                if nuevo_rol in ["admin", "usuario"]:
                    usuario.rol = nuevo_rol
                    print(" Rol actualizado.")
                else:
                    print(" Rol inválido.")
            else:
                print(" Usuario no encontrado.")
        elif opcion == "3":
            nombre = input("Ingrese usuario a eliminar: ")
            usuario = buscar_usuario(nombre, lista_usuarios)
            if usuario:
                lista_usuarios.remove(usuario)
                print(" Usuario eliminado.")
            else:
                print(" Usuario no encontrado.")
        elif opcion == "4":
            break
        else:
            print(" Opción inválida.")
