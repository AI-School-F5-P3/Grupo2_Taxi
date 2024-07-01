# bibliotecas para gestionar ficheros y generar ficheros csv
import os, csv

#Utilería de generación de número consecutivo de carrera
def generar_numero_carrera(nombre_fichero) -> int:
    #ubicación es la ruta desde donde se ejecuta el código junto con el nombre de fichero propuesto.
    ubicacion = os.path.join(os.path.dirname(__file__),nombre_fichero)
    
    try:
        #intento de apertura del fichero donde se almacena el consecutivo de carrera
        with open(ubicacion, 'r') as file:
            ultima_carrera = int(file.read().strip())
    #Excepciones de fichero no encontrado, En ese caso, el conteo comenzara desde 0
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        ultima_carrera = 0
    #Incrementar el valor de la última carrera en 1. Si no hay antecedente, el número de carrera comenzará en 1.
    ultima_carrera += 1

    try:
        #Intento de escritura del fichero con el número de la última carrera
        with open(ubicacion, 'w') as file:
            file.write(str(ultima_carrera))
    #Excepciones de fichero no encontrado.   
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        print("Error al leer el archivo.")
    #Entregar el valor de la última carrera que debe utilizarse a la llamada de este procedimiento
    return ultima_carrera     
