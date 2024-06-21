
def salir(self):
     while True:
        
        confirmacion = input('¿seguro que deseas cerrar? Si estás seguro pulsa de nuevo 3')
        if confirmacion == 3:
            print('Sales de la aplicación. Hasta pronto')
            break
        else:
            def mostrar_menu():
