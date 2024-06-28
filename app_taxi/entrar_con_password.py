import json
import os
import mostrar_menu
import logging
import shared
import csv

archivo_usuarios = 'usuarios.json'

class Usuario():
    def __init__(self, nombre, contraseña):
        self.nombre = nombre # Nombre de usuario
        self.contraseña = contraseña # Contraseña
        
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
        logging.warning('No se encuentra el archivo de usuarios.') # Advertencia si no se encuentra el archivo
        return []
    except json.JSONDecodeError: 
        logging.error('Error al decodificar el archivo JSON de usuarios.') # Error si hay un problema al decodificar JSON
        return []
    
    # Función para enviar solicitud de registro
def solicitar_registro():
    # Matrícula
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

    # DNI o NIE
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

    # Nombre
    nombre = input("Introduce tu nombre: ")
    limpiar_consola()

    # Apellidos
    apellidos = input("Introduce tus apellidos: ")

    # Correo electrónico
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

    # Número de teléfono
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
        # Abrir el archivo en modo de append... "append" significa que se abre el archivo para añadir datos al final del archivo existente, en lugar de sobrescribir los datos existentes o leerlos.
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
 
 # Función para verificar la contraseña de un usuario
def verificar_contraseña(nombre_usuario, password_introducida):
    usuarios = cargar_usuarios() # Cargar la lista de usuarios registrados
    
    # Recorrer la lista de usuarios para buscar el usuario por su nombre
    for usuario in usuarios:
        if usuario.nombre == nombre_usuario:
            # Si se encuentra el usuario, verificar si la contraseña es correcta
            if usuario.contraseña == password_introducida:
                input('Contraseña correcta')
                logging.info('Contraseña correcta')
                return usuario
            else:
                print('¡La contraseña no es correcta!')
                logging.warning('Contraseña incorrecta.')
                return None  # Contraseña incorrecta
    print('Usuario no encontrado en la lista.')  # Mensaje de error si el usuario no se encuentra
    logging.warning('Usuario no encontrado en la lista.')  # Registrar error en el log
    return None  # Retornar None si el usuario no se encuentra

# Bucle para el menú de incio
def menu_principal():
    while True:
        # 3 opciones para el usuario
        print("\nSelecciona una opción:")
        print("1. Iniciar sesión")
        print("2. Solicitar registro")
        print("3. Salir")
        
        opcion = input("Opción: ") # Lee la opción seleccionada por el usuario
        
        if opcion == "1":
            # Iniciar sesión
            nombre_usuario_a_verificar = input("Introduce el nombre de usuario: ")
            password_a_verificar = input("Introduce la contraseña: ")
            usuario_valido = verificar_contraseña(nombre_usuario_a_verificar, password_a_verificar) # Verificar las credenciales del usuario
            if usuario_valido:
                shared.usuario_activo = usuario_valido.nombre  # Establecer el usuario activo
                logging.info('Inicio de sesión exitoso para %s', usuario_valido.nombre)  # Registrar éxito en el log
                mostrar_menu.mostrar_menu()  # Mostrar el menú después del inicio de sesión
            else:
                print("Inicio de sesión fallido. Verifica tus credenciales.")  # Mensaje de error si las credenciales son incorrectas
                logging.warning('Inicio de sesión fallido para %s', nombre_usuario_a_verificar)  # Registrar error en el log
        elif opcion == "2":
            solicitar_registro()
        elif opcion == "3":
            print("Saliendo...")
            logging.info('Saliendo del programa.')
            os._exit(0) # Terminar el programa
        else:
            # Mensaje de error si la opción seleccionada no es válida
            print("Opción no válida. Por favor, intenta de nuevo.")
            logging.warning('Opción no válida en el menú principal.') # Registrar error en el log

if __name__ == "__main__":
    menu_principal()