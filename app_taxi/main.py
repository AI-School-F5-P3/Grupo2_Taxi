import saludar
import mostrar_menu
import entrar_con_password
import logging
import sys

#configuración de log general, dentro de los paréntesis se codifica cómo quiero que me devuelva la información, level = el nivel a partir del cual quiero que me envía los mensajes. 
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename = 'log_taxi.log', 
                    filemode = 'a')
#esta configuración es para que detecte y registre en el archivo log todos los posibles errores que no se registran a mano a lo largo del código con logging.debug o logging.error (por ejemplo)
def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("excepcion no recogida", exc_info=(exc_type, exc_value, exc_traceback))
sys.excepthook = handle_exception

saludar.saludar()  # Saluda al usuario al inicio del programa
entrar_con_password.menu_principal()  # Intenta iniciar sesión primero
    
    # Después del inicio de sesión exitoso, muestra el menú principal

mostrar_menu.mostrar_menu()