import os

def limpiar_consola():
    # Limpia la consola
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS y Linux
        os.system('clear')
def solicitar_opcion():
    while True:
        try:
            option = int(input('Por favor elija una opción (número del 1 al 3): '))
            if 1 <= option <= 3:
                return option
            else:
                print('Por favor, elija un número entre 1 y 3.')
        except ValueError:
            print('Entrada no válida. Por favor, introduzca un número entero del 1 al 3.')
def mostrar_menu_config():
    mensaje_config =''
    
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
        
        option = solicitar_opcion()
        
        
        limpiar_consola()
        
        if option == 1:
            mensaje_config='Cambiar conductor'             
            #cambiar_conductor()
            
            
           
        elif option == 2: 
           mensaje_config= 'Cambiar tarifas'
           #cambiar_tarifa()
        elif option == 3:
            mensaje_config = 'Volver a la aplicación'
            mostrar_menu()
        
            #salir()
def mostrar_menu():
    mensaje =''
    
    while True:
        limpiar_consola()
        
        menu = (
        '   MENU GENERAL  \n'
        '1. Configuración\n'
        '2. Comenzar carrera\n'
        '3. Salir de la aplicación\n'
    )
    
        print(menu)
        
        print(mensaje)
        
        option = solicitar_opcion()
        
        
        limpiar_consola()
        
        if option == 1:
            mensaje='Configurar'             
            mostrar_menu_config()
            
            
           
        elif option == 2: 
           mensaje= 'Comienza una carrera'
           #cambiar_tarifa()
        elif option == 3:
            mensaje = 'Vas a salir de la aplicación'
            #salir()

mostrar_menu()            
   