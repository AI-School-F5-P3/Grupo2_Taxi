import saludar
import entrar_con_password
import mostrar_menu
import logging
import sys
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename = 'log_taxi.log', 
                    filemode = 'a')
def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("excepcion no recogida", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
logger = logging.getLogger(__name__)
saludar.saludar()
entrar_con_password.entrar_con_password()
mostrar_menu.mostrar_menu()