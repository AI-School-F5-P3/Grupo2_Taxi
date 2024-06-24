import saludar
import entrar_con_password
import mostrar_menu
import datetime
import logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename = 'log_taxi.log', 
                    filemode = 'a')
saludar.saludar()
entrar_con_password.entrar_con_password()
mostrar_menu.mostrar_menu()
