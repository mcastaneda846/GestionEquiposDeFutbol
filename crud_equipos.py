equipos = []


def crear_equipo():
    while True:
        nombre = input("Nombre del equipo: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío.\n")
        else:
            equipos.append({"nombre": nombre})
            print("Equipo agregado.\n")
            break


def listar_equipos():
    if len(equipos) == 0:
        print("No hay equipos registrados.\n")
        return

    print("\n--- Equipos Registrados ---\n")
    for i, eq in enumerate(equipos):
        print(f"{i+1}. {eq['nombre']}")
    print()


def actualizar_equipo():
    listar_equipos()
    if len(equipos) == 0:
        return

    while True:
        indice = input("Número del equipo a actualizar: ").strip()

        if not indice.isdigit():
            print("Debe ingresar un número que se encuentre en la lista.\n")
            continue

        indice = int(indice) - 1

        if indice < 0 or indice >= len(equipos):
            print("Número fuera de rango.\n")
        else:
            break

    while True:
        nuevo_nombre = input("Nuevo nombre: ").strip()
        if nuevo_nombre == "":
            print("El nombre no puede estar vacío.\n")
        else:
            equipos[indice]["nombre"] = nuevo_nombre
            print("Equipo actualizado.\n")
            break


def eliminar_equipo():
    listar_equipos()
    if len(equipos) == 0:
        return

    while True:
        indice = input("Número del equipo a eliminar: ").strip()

        if not indice.isdigit():
            print("Debe ser un número que se encuentre en la lista.\n")
            continue

        indice = int(indice) - 1

        if indice < 0 or indice >= len(equipos):
            print("Número fuera de rango.\n")
        else:
            equipos.pop(indice)
            print("Equipo eliminado.\n")
            break
