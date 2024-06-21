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
            option = int(input('Por favor elija una opción (número del 1 al 5): '))
            if 1 <= option <= 5:
                return option
            else:
                print('Por favor, elija un número entre 1 y 5.')
        except ValueError:
            print('Entrada no válida. Por favor, introduzca un número entero.')

def mostrar_menu():
    mensaje =''
    ultima_opcion = None
    while True:
        limpiar_consola()
        
        menu = (
        '   MENU   \n'
        '1. Nueva carrera\n'
        '2. Moverse\n'
        '3. Parar\n'
        '4. Fin de carrera\n'
        '5. Salir de la aplicación\n'
    )
    
        print(menu)
        
        print(mensaje)
        
        option = solicitar_opcion()
        
        if option == ultima_opcion:
            print('No puede seleccionar la misma opción dos veces consecutivas. Por favor, elija otra opción.')
            input('Presione Enter para continuar...')
            continue 
        limpiar_consola()
        
        if option == 1:
            if ultima_opcion == 2 or ultima_opcion == 3:
                print('El coche ya está en movimiento, si quieres iniciar una carrera, finaliza la actual (pulsa 4) ')
                input('Presione Enter para continuar...')
                continue 
            elif ultima_opcion == 3:
                print('El coche está parado pero arrancado, si quieres iniciar una carrera, finaliza la actual (pulsa 4) ')
                input('Presione Enter para continuar...')
                continue
            else:
                #iniciar()
                mensaje='Motor arrancado (el coche está parado)'
                continue
           
        elif option == 2: 
            if ultima_opcion == 4:
                print('Opcion no valida. La carrera finalizó. Pulsa 1 para una nueva carrera ó 5 para salir')
                input('Presione Enter para continuar...')
                continue 
                       
            else:
                #estar_moviento()
                mensaje='El coche está en movimiento'
        elif option == 3:
            if ultima_opcion == 4:
                print('Opcion no valida. La carrera finalizó. Pulsa 1 para una nueva carrera ó 5 para salir')
                input('Presione Enter para continuar...')
                continue 
                       
            else:
             #estar_parado()
                mensaje = 'El coche vuelve a estar parado, pero arrancado'
        elif option == 4:
            print('Fin de la carrera. Se apaga el motor')
            mensaje = 'Fin de la carrera. Se apaga el motor'
        
        elif option == 5:
            print('Sales de la aplicación. Hasta pronto')
            break
        else:
            print('Opción no válida, por favor elija un número del 1 al 5.')
        
        #input('Presione Enter para continuar...')
        ultima_opcion = option