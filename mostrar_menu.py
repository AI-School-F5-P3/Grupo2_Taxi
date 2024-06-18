def mostrar_menu(): 
    while True :
    
        print('   MENU   ')
        print('1. Empezar carrera')
        print('2. Moverse')
        print('3. Parar')
        print('4. Fin de carrera')
        print('5. Nueva carrera')
        print('6. Salir de la aplicación')
        option = int(input('por favor elija una opción (número del 1 al 6)'))
        
        if option == 1:
        #inicio()
            print('Comienza la carrera, con el coche parado')
        elif option == 2: 
        #movimiento()
            print('Coche en movimiento')
        elif option == 3:
        #parada()
            print('El coche vuelve a estar parado')
        elif option == 4:
        #final()
            print('Fin de la carrera')
        elif option == 5:
        #inicio()
            print('Nueva carrera')
        elif option == 6:
            print('Sales de la aplicación. Hasta pronto')
            break
        else:
            print('Opción no válida, por favor elija un número del 1 al 6.')