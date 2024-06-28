import json
import os
import mostrar_menu
import logging
import shared

archivo_usuarios = 'usuarios.json'

class Usuario():
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

def cargar_usuarios():
    try:
        with open(archivo_usuarios, 'r', encoding='utf-8') as file:
            usuarios_data = json.load(file)
            usuarios = []
            for usuario_data in usuarios_data:
                usuarios.append(Usuario(usuario_data["usuario"], usuario_data["contraseña"]))
            return usuarios
    except FileNotFoundError:
        logging.warning('No se encuentra el archivo de usuarios.')
        return []
    except json.JSONDecodeError:
        logging.error('Error al decodificar el archivo JSON de usuarios.')
        return []

def guardar_usuarios(usuarios):
    with open(archivo_usuarios, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, indent=4)
    logging.info('usuario guardado correctamente')

def verificar_contraseña(nombre_usuario, password_introducida):
    usuarios = cargar_usuarios()
    
    for usuario in usuarios:
        if usuario.nombre == nombre_usuario:
            if usuario.contraseña == password_introducida:
                input('Contraseña correcta')
                logging.info('Contraseña correcta')
                return usuario
            else:
                print('¡La contraseña no es correcta!')
                logging.warning('Contraseña incorrecta.')
                return None  # Contraseña incorrecta
    print('Usuario no encontrado en la lista.')
    logging.warning('Usuario no encontrado en la lista.')
    return None  # Usuario no encontrado

def menu_principal():
    while True:
        print("\nSelecciona una opción:")
        print("1. Iniciar sesión")
        print("2. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            nombre_usuario_a_verificar = input("Introduce el nombre de usuario: ")
            
            password_a_verificar = input("Introduce la contraseña: ")
            usuario_valido = verificar_contraseña(nombre_usuario_a_verificar, password_a_verificar)
            if usuario_valido:
                shared.usuario_activo = usuario_valido.nombre
                logging.info('Inicio de sesión exitoso para %s', usuario_valido.nombre)
                mostrar_menu.mostrar_menu()  # Aquí deberías llamar a la función que muestra el menú después del inicio de sesión
            else:
                print("Inicio de sesión fallido. Verifica tus credenciales.")
                logging.warning('Inicio de sesión fallido para %s', nombre_usuario_a_verificar)
        elif opcion == "2":
            print("Saliendo...")
            logging.info('Saliendo del programa.')
            os._exit(0)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            logging.warning('Opción no válida en el menú principal.')

if __name__ == "__main__":
    menu_principal()