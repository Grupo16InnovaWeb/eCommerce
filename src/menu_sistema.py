# menu_sistema.py
class MenuSistema:
    def mostrar_menu_usuario(self, usuario):
        print("\nMENÚ DE USUARIO")
        print(usuario.mostrar_datos())

    def mostrar_menu_admin(self, auth):
        while True:
            print("\nMENÚ ADMINISTRADOR")
            print("1. Ver usuarios")
            print("2. Cambiar rol")
            print("3. Eliminar usuario")
            print("4. Salir")
            opcion = input("Opción: ")

            if opcion == "1":
                for u in auth.lista_usuarios:
                    print(u.mostrar_datos())

            elif opcion == "2":
                nombre = input("Usuario a modificar: ")
                usuario = auth.buscar_usuario(nombre)
                if usuario:
                    nuevo_rol = input("Nuevo rol (admin/usuario): ")
                    if nuevo_rol in ["admin", "usuario"]:
                        usuario.rol = nuevo_rol
                        print("Rol actualizado.")
                    else:
                        print("Rol inválido.")
                else:
                    print("Usuario no encontrado.")

            elif opcion == "3":
                nombre = input("Usuario a eliminar: ")
                usuario = auth.buscar_usuario(nombre)
                if usuario:
                    if usuario.nombre_usuario == "admin":
                        print("No se puede eliminar al admin por defecto.")
                    else:
                        auth.lista_usuarios.remove(usuario)
                        print("Usuario eliminado.")
                else:
                    print("Usuario no encontrado.")

            elif opcion == "4":
                break
            else:
                print("Opción inválida.")
