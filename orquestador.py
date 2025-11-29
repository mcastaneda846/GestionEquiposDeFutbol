from login import cargar_usuarios, validar_login, crear_cuenta
from crud_equipos import (
    crear_equipo,
    listar_equipos,
    actualizar_equipo,
    eliminar_equipo
)

def menu_inicial():
    print("""
-------- MENÚ PRINCIPAL --------
1. Iniciar sesión
2. Crear cuenta
3. Salir
""")


def menu_crud():
    print("""
-------- CRUD DE EQUIPOS --------
1. Crear equipo
2. Listar equipos
3. Actualizar equipo
4. Eliminar equipo
5. Cerrar sesión
""")


def main():
    while True:
        menu_inicial()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            usuarios = cargar_usuarios()
            if validar_login(usuarios):

                while True:
                    menu_crud()
                    op = input("Opción: ").strip()

                    if op == "1":
                        crear_equipo()
                    elif op == "2":
                        listar_equipos()
                    elif op == "3":
                        actualizar_equipo()
                    elif op == "4":
                        eliminar_equipo()
                    elif op == "5":
                        print("Sesión cerrada.\n")
                        break
                    else:
                        print("Opción inválida.\n")
            else:
                break

        elif opcion == "2":
            crear_cuenta()

        elif opcion == "3":
            print("Saliendo del programa... ¡Hasta luego!")
            break

        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    main()
