import os
''' os es una biblioteca estándar que proporciona una interfaz
para interactuar con el sistema operativo en el que se ejecuta el programa'''
import servicio
import entrar_con_password
import logging
import shared
import reportes



def limpiar_consola(): 
    # limpiar_consola(), borra lo que haya en consola (para tener sólo un menú impreso en consola)
    if os.name == 'nt':
        os.system('cls') # Windows
    else:
        os.system('clear') # Unix/Linux/MacOS

def solicitar_opcion():
    '''solicitar_opcion() hace que cuando se imprime un menú pide elegir una opción y gestiona que se a válida dicha opción,
    devuelve un valor para la variable local option'''
    while True:
        try:
            option = int(input('Por favor elija una opción (número del 1 al 3): '))
            if 1 <= option <= 3:
                return option
            else:
                logging.warning('Opción no válida')
                print('Por favor, elija un número entre 1 y 3.')
        except ValueError:
            logging.warning('Opción no válida')
            print('Entrada no válida. Por favor, introduzca un número entero del 1 al 3.')
def solicitar_opcion_4ops():
    '''solicitar_opcion_4ops() hace que cuando se imprime un menú pide elegir una opción
    y gestiona que se a válida dicha opción. Devuelve un valor para la variable local option'''
    while True:
        try:
            option = int(input('Por favor elija una opción (número del 1 al 4): '))
            if 1 <= option <= 4:
                return option
            else:
                logging.warning('opcion no válida')
                print('Por favor, elija un número entre 1 y 4.')
        except ValueError:
            logging.warning('opcion no válida')
            print('Entrada no válida. Por favor, introduzca un número entero del 1 al 4.')

def mostrar_menu_config():
    '''limpia la consola, despliega el menú de configuración,
    solicita elegir una opción,
    muestra un mensaje según la opción elegida'''
    mensaje_config = ''
    
    while True:
        limpiar_consola()
        
        menu_config = (
            '   MENU CONFIGURACIÓN   \n'
            '1. Cambiar conductor\n'
            '2. Cambiar tarifas\n'
            '3. Volver al menú general\n'
        )
    
        print(menu_config)
        print(mensaje_config)
        logging.debug('abre el menu_config')
        option = solicitar_opcion()
        
        limpiar_consola()
        
        if option == 1:
            mensaje_config = 'Cambiar conductor'
            entrar_con_password.menu_principal()  # Llama al inicio de sesión nuevamente
            logging.debug('vuelvo al menu principal, cambio conductor')
        elif option == 2:
            if shared.usuario_activo == "Administrador":
                mensaje_config = 'Cambiar tarifas'
                servicio.cambiar_tarifa()  # Lógica para cambiar tarifas
                input("Presiona Enter para volver al menú principal...")
                logging.debug('Regreso al menú principal después de cambiar tarifas')
            else:
                input("No tienes acceso a esta función. Presiona Enter para volver al menú principal...")
                logging.warning('Intento de cambiar tarifas sin permisos de administrador')
        elif option == 3:
            mensaje_config = 'Volver al menú general'
            logging.debug('sale de menu_config, vuelve a menu principal')
            break  # Salir de este menú y volver al menú general

def mostrar_menu():
    '''limpia la consola, despliega el menú general,
    solicita elegir una opción,
    muestra un mensaje según la opción elegida'''
    mensaje = ''
    
    while True:
        limpiar_consola()
        
        menu = (
            '   MENU GENERAL  \n'
            '1. Configuración\n'
            '2. Comenzar carrera\n'
            '3. Consultar informes\n'
            '4. Salir de la aplicación\n'
        )
    
        print(menu)
        print(mensaje)
        
        option = solicitar_opcion_4ops()
        
        limpiar_consola()
        
        if option == 1:
            mensaje = 'Configurar'
            logging.info('cambio a menu_config')
            mostrar_menu_config()
        elif option == 2:
            mensaje = 'Comienza una carrera'
            logging.info('comienza una carrera')
            servicio.iniciar()
        elif option == 3:
            if shared.usuario_activo == "Administrador":
                mensaje = 'Generando informe'
                logging.info('generando informe')
                reportes.Reportes.generar_grafica()
                input("Presiona Enter para volver al menú principal...")
                logging.debug('Se muestran informes')
            else:
                input("No tienes acceso a esta función. Presiona Enter para volver al menú principal...")
                logging.warning('Intento de genenerar informes sin permisos de administrador')
            
        elif option == 4:
            mensaje = 'Vas a salir de la aplicación'
            while True:
                confirmacion = input('¿Seguro que deseas cerrar? Si estás seguro pulsa de nuevo 4: ')
                if confirmacion != "4":
                    print('Vuelves al menú princial')
                    input('Presiona enter para continuar...')
                    mostrar_menu()
                else:
                    print('Sales de la aplicación. Hasta pronto')
                    logging.debug('sales de la aplicación')
                    os._exit(0)