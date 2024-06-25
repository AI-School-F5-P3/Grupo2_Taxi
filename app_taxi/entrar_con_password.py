import json
import os
import mostrar_menu
import logging

archivo_usuarios = 'usuarios.json'

def cargar_usuarios():
    try:
        with open(archivo_usuarios, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning('no se encuentra el archivo')
        return []

def guardar_usuarios(usuarios):
    with open(archivo_usuarios, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, indent=4)
    logging.info('usuario guardado correctamente')

def verificar_contraseña(nombre_usuario, password_introducida):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["usuario"] == nombre_usuario:
            if usuario["contraseña"] == password_introducida:
                print('Contraseña correcta')
                logging.info('contraseña correcta')
                return True
            else:
                print('¡La contraseña no es correcta!')
                logging.warning('contraseña incorrecta')
                return False
    print('Usuario no encontrado.')
    logging.warning('usuario no encontrado')
    return False

def menu_principal():
    while True:
        print("\nSelecciona una opción:")
        print("1. Iniciar sesión")
        print("2. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            nombre_usuario_a_verificar = input("Introduce el nombre de usuario: ")
            password_a_verificar = input("Introduce la contraseña: ")
            if verificar_contraseña(nombre_usuario_a_verificar, password_a_verificar):
                logging.info('contraseña verificada')
                mostrar_menu.mostrar_menu()
                break
        elif opcion == "2":
            print("Saliendo...")
            print('Sales de la aplicación. Hasta pronto')
            logging.info('sale de la aplicación')
            os._exit(0)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            logging.warning('opcion de menu principal no válida')

if __name__ == "__main__":
    menu_principal()
