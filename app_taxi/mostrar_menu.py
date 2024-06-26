import os
import servicio
import entrar_con_password
import logging
import shared
import reportes

#Método de cambio de tarifa
def cambiar_tarifa():
    #Cambio de tarifa en parada
    while True:
        nueva_tarifa_parada = input('Introduzca nueva tarifa diurna de parada (la nocturna duplica este valor) : ')
        try:
            #nueva_tarifa_parada = float(nueva_tarifa_parada)
            shared.tarifa_parada = float(nueva_tarifa_parada)
            shared.tarifa_parada_nocturna = float(nueva_tarifa_parada) * 2
            break
        except ValueError:
            logging.warning('Método de cambio de tarifa: El valor ingresado no es del tipo float')
            print('Entrada no válida. Inténtelo nuevamente')

    #Cambio de tarifa en movimiento        
    while True:
        nueva_tarifa_movimiento = input('Introduzca nueva tarifa diurna en movimiento (la nocturna duplica este valor) : ')
        try:
            #nueva_tarifa_movimiento = float(nueva_tarifa_movimiento)
            shared.tarifa_movimiento = float(nueva_tarifa_movimiento)
            shared.tarifa_movimiento_nocturna = float(nueva_tarifa_movimiento) * 2
            break
        except ValueError:
            logging.warning('Método de cambio de tarifa: El valor ingresado no es del tipo float')
            print('Entrada no válida. Inténtelo nuevamente')
#Fin de método de cambio de tarifa

def limpiar_consola(): #Limpia la consola
    if os.name == 'nt':
        os.system('cls') #Windows
    else:
        os.system('clear') #IOs

def solicitar_opcion():
    while True:
        try:
            option = int(input('Por favor elija una opción (número del 1 al 3): '))
            if 1 <= option <= 3:
                return option
            else:
                logging.warning('opcion no válida')
                print('Por favor, elija un número entre 1 y 3.')
        except ValueError:
            logging.warning('opcion no válida')
            print('Entrada no válida. Por favor, introduzca un número entero del 1 al 3.')
def solicitar_opcion_4ops():
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
            mensaje_config = 'Cambiar tarifas'  # Lógica para cambiar tarifas
            cambiar_tarifa()
        elif option == 3:
            mensaje_config = 'Volver al menú general'
            logging.debug('sale de menu_config, vuelve a menu principal')
            break  # Salir de este menú y volver al menú general

def mostrar_menu():
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
            mensaje = 'Generando informe'
            logging.info('generando informe')
            reportes.generar_grafica()
        elif option == 4:
            mensaje = 'Vas a salir de la aplicación'
            while True:
                confirmacion = input('¿Seguro que deseas cerrar? Si estás seguro pulsa de nuevo 4: ')
                if confirmacion != "4":
                    continue
                else:
                    print('Sales de la aplicación. Hasta pronto')
                    logging.debug('sales de la aplicación')
                    os._exit(0)
