
#---------------- | Importación de librerías a usar en ESTE fichero |------------------------------------------------------------
import json #Importación del módulo de Json para abrir, crear y guardar los registros recogidos en dataframe de los "viajes"
import os   #Para usar funcionalidades del sistema
import logging #Para que se realice logs
import shared #Al jacer import shared se le usa para traer o utilizar funciones que hay en otros ficheros






#---------------- | Importación del archivo "mostrar_menu.py" |------------------------------------------------------------------

import mostrar_menu #Trae todas las funciones creadas en ese fichero





#----------------|  Establecimiento de las clases y funciones |----------------------------------------------------------------
#---Aquí se definen las variables, los procesos y las funciones que en conjunto van a permitir la autentificación de usuario


archivo_usuarios = 'usuarios.json' #En esta variable guardamos el fichero 'usuarios.jason' que es donde se irán alamacenando los usuarios a medida que el Admin los cree.

#------Creación de la clase Usuario()
class Usuario():        
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña



#------Función que coge la variable donde se almacena el fichero de json a usar, lo carga para lectura.
#para ver la lectura del jason, se le llama a la clase Usuario() metiéndole como atributo la carga del 
#fichero, tanto en usuario(que es el nombre) como en "contraseña"(que es contraseña)

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


#------Función que coge la variable donde se almacena el fichero de json a usar, lo carga para escritura.
#Coge el return de la anterior función, que es 'usuarios', y lo guarda

def guardar_usuarios(usuarios):
    with open(archivo_usuarios, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, indent=4)
    logging.info('usuario guardado correctamente')


#------Función que se verifican las contraseñas

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


#------Función donde se van a llamar  a las funciones creadas anteriormente para autentificar el usuario
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