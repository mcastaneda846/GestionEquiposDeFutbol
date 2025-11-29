import csv
import os

# 1. Verificar si existe el CSV, si no crearlo

def verificar_o_crear_csv():
    if not os.path.exists("usuarios.csv"):
        with open("usuarios.csv", "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["username", "password"])
        print("Archivo 'usuarios.csv' creado automáticamente.\n")


# Cargar usuarios del CSV
def cargar_usuarios():
    verificar_o_crear_csv()  # Asegura que existe

    usuarios = []
    with open("usuarios.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            usuarios.append({
                "username": fila["username"],
                "password": fila["password"]
            })
    return usuarios


# Login con máximo 3 intentos
def validar_login(usuarios):
    intentos = 3

    while intentos > 0:
        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()

        if usuario == "" or contraseña == "":
            print("Ningún campo puede estar vacío.\n")
            continue

        for u in usuarios:
            if u["username"] == usuario and u["password"] == contraseña:
                print("\n¡Login exitoso!\n")
                return True

        intentos -= 1
        print("Credenciales incorrectas. Intentos restantes:", intentos, "\n")

    print("Has agotado los intentos. El programa se cerrará.")
    return False


# Funciones para crear cuenta
def pedir_usuario_nuevo(usuarios):
    while True:
        nuevo = input("Nuevo usuario: ").strip()

        if nuevo == "":
            print("El usuario no puede estar vacío.\n")
            continue

        repetido = False
        for u in usuarios:
            if u["username"] == nuevo:
                repetido = True
                break

        if repetido:
            print("Ese usuario ya existe.\n")
        else:
            return nuevo


def pedir_contraseña_nueva():
    while True:
        contraseña = input("Nueva contraseña: ").strip()
        if contraseña == "":
            print("La contraseña no puede estar vacía.\n")
        else:
            return contraseña


def guardar_usuario(usuario, contraseña):
    with open("usuarios.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([usuario, contraseña])


# Crear cuenta con funciones separadas
def crear_cuenta():
    usuarios = cargar_usuarios()

    nuevo_usuario = pedir_usuario_nuevo(usuarios)
    nueva_contraseña = pedir_contraseña_nueva()

    guardar_usuario(nuevo_usuario, nueva_contraseña)

    print("\nCuenta creada exitosamente.\n")

