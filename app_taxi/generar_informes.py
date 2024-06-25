import os, csv, datetime, pytz

fichero_contador = 'contador_carreras.txt'
fichero_carreras = 'carreras.csv'

def generar_numero_carrera(nombre_fichero) -> int:
    ubicacion = os.path.join(os.path.dirname(__file__),nombre_fichero)
    try:
        with open(ubicacion, 'r') as file:
            ultima_carrera = int(file.read().strip())         
    except IOError:
        ultima_carrera = 0
    ultima_carrera += 1
    with open(ubicacion, 'w') as file:
        file.write(str(ultima_carrera))
    return ultima_carrera     
