import saludar
def entrar_con_password():
    password = ''
    password_confirmada = ''
    
    password = input('Crea una contraseña: ')
    while continuar:
        
        password_confirmada = input('Intruduce tu contraseña: ')
        if password_confirmada != password:
            print('¡La contraseña no es correcta!')
        else:
            print('aquí el método de bienvenida')
            
            break
    continuar = False
    saludar.saludar()        
            

        
        