import os, csv

#Utilería de generación de consecutivo
def generar_numero_carrera(nombre_fichero) -> int:
    ubicacion = os.path.join(os.path.dirname(__file__),nombre_fichero)
    try:
        with open(ubicacion, 'r') as file:
            ultima_carrera = int(file.read().strip())         
    except FileNotFoundError:
        print("El archivo no existe.")
    
    except IOError:
        ultima_carrera = 0
    ultima_carrera += 1
    try:
        with open(ubicacion, 'w') as file:
            file.write(str(ultima_carrera))
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        print("Error al leer el archivo.")
    return ultima_carrera     
