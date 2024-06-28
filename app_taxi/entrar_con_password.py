import json
import os
import mostrar_menu
import logging
import shared
import csv

archivo_usuarios = 'usuarios.json'

class Usuario():
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        
def limpiar_consola(): 
    # limpiar_consola(), borra lo que haya en consola (para tener sólo un menú impreso en consola)
    if os.name == 'nt':
        os.system('cls') # Windows
    else:
        os.system('clear') # Unix/Linux/MacOS

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
    
    
def solicitar_registro():
    # Solicitar y confirmar matrícula
    while True:
        limpiar_consola()
        matricula = input("Introduce tu matrícula: ")
        confirmar = input(f"Has introducido '{matricula}'. ¿Es correcto? (Sí/No): ")
        if confirmar.lower() == 'sí':
            break
        elif confirmar.lower() == 'si':
            break
        elif confirmar.lower() == 'no':
            print("Vamos a volver a intentarlo.")

    # Solicitar y confirmar DNI o NIE
    while True:
        limpiar_consola()
        dni_nie = input("Introduce tu DNI o NIE: ")
        confirmar = input(f"Has introducido '{dni_nie}'. ¿Es correcto? (Sí/No): ")
        if confirmar.lower() == 'sí':
            break
        elif confirmar.lower() == 'si':
            break
        elif confirmar.lower() == 'no':
            print("Vamos a volver a intentarlo.")

    # Solicitar nombre
    nombre = input("Introduce tu nombre: ")

    # Solicitar apellidos
    apellidos = input("Introduce tus apellidos: ")

    # Solicitar y confirmar correo electrónico
    while True:
        limpiar_consola()
        correo = input("Introduce tu correo electrónico: ")
        confirmar = input(f"Has introducido '{correo}'. ¿Es correcto? (Sí/No): ")
        if confirmar.lower() == 'sí':
            break
        elif confirmar.lower() == 'si':
            break
        elif confirmar.lower() == 'no':
            print("Vamos a volver a intentarlo.")

    # Solicitar y confirmar número de teléfono
    while True:
        limpiar_consola()
        telefono = input("Por último, introduce tu número de teléfono para que nos podamos comunicar contigo: ")
        confirmar = input(f"Has introducido '{telefono}'. ¿Es correcto? (Sí/No): ")
        if confirmar.lower() == 'sí':
            break
        elif confirmar.lower() == 'si':
            break
        elif confirmar.lower() == 'no':
            print("Vamos a volver a intentarlo.")  
    guardar_solicitud(matricula, dni_nie, nombre, apellidos, correo, telefono)
    print("Gracias por tu tiempo. Tu solicitud ha sido enviada con éxito.") 
    input("Taxiter se pondrá en contacto contigo a través del teléfono facilitado en un plazo de 48h.")
            
def guardar_solicitud(matricula, dni_nie, nombre, apellidos, correo, telefono):
    # Definir la ruta del archivo de solicitudes
    file_path = 'nuevas_solicitudes.csv'
    # Verificar si el archivo ya existe
    file_exists = os.path.isfile(file_path)

    try:
        # Abrir el archivo en modo de append
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            # Si el archivo no existe, escribir la cabecera
            if not file_exists:
                writer.writerow(['Matrícula', 'DNI/NIE', 'Nombre', 'Apellidos', 'Correo Electrónico', 'Teléfono'])
            # Escribir los datos de la solicitud
            writer.writerow([matricula, dni_nie, nombre, apellidos, correo, telefono])
    except Exception as e:
        logging.error(f"Error al guardar la solicitud: {e}")
        print("Ocurrió un error al guardar la solicitud. Por favor, inténtalo de nuevo.")

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
        print("2. Solicitar registro")
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
            solicitar_registro()
        elif opcion == "3":
            print("Saliendo...")
            logging.info('Saliendo del programa.')
            os._exit(0)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            logging.warning('Opción no válida en el menú principal.')

if __name__ == "__main__":
    menu_principal()