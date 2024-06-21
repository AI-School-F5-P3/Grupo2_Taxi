def entrar_con_password():
    password = input('Crea una contraseña: ')
    while True:
        password_confirmada = input('Intruduce tu contraseña: ')
        if password_confirmada != password:
            print('¡La contraseña no es correcta!')
        else:
            print('Contraseña correcta')
            break
    

      
            

        
        