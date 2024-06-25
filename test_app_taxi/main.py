import saludar
import mostrar_menu
import entrar_con_password

saludar.saludar()  # Saluda al usuario al inicio del programa
entrar_con_password.menu_principal()  # Intenta iniciar sesión primero
    
    # Después del inicio de sesión exitoso, muestra el menú principal
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename = 'log_taxi.log', 
                    filemode = 'a')
def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("excepcion no recogida", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
logger = logging.getLogger(__name__)
mostrar_menu.mostrar_menu()