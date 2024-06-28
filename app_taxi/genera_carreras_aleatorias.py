import csv
import random
import numpy as np
from datetime import datetime, timedelta
#dado que no tenemos datos reales, para mostrar la posibilidad de crear gráficos, se crea una función que genere carreras aleatorias en un periodo de 6 meses
def generar_datos_csv():
    conductores = ['Nathaly', 'Carolina', 'Sergio', 'Angel', 'Jorge'] 
    probabilidades = [0.1, 0.22, 0.15, 0.32, 0.21] 
    inicio = datetime.now() - timedelta(days=170)  # Hace 6 meses

    with open('datos.csv', 'w', newline='') as csvfile:   #hace referencia a dónde va a guardar los datos, que solo la accion es escritura 
        fieldnames = ['carrera', 'conductor', 'inicio_carrera', 'fin_carrera', 'precio_total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)   
        writer.writeheader()   #con los valores de la lista, escribe la primera línea del archivo csv. 

        for carrera in range(1, 10001):
            segundos_aleatorios = random.randint(0, 170*24*60*60)  # Minutos aleatorios en los últimos 6 meses
            inicio_carrera = inicio + timedelta(seconds=segundos_aleatorios)
            duracion_viaje = random.randint(300, 2400)  # Duración del viaje en minutos
            fin_carrera = inicio_carrera + timedelta(seconds=duracion_viaje)
            precio_total = round(duracion_viaje * 0.02, 2)  # Precio basado en la duración del viaje
            conductor = np.random.choice(conductores, p=probabilidades)
            #ahora con todo lo generado en las líneas anteriores, se manda linea a linea al archivo csv
            writer.writerow({'carrera': carrera, 'conductor': conductor, 'inicio_carrera': inicio_carrera.strftime('%Y-%m-%d %H:%M:%S'), 'fin_carrera': fin_carrera.strftime('%Y-%m-%d %H:%M:%S'), 'precio_total': precio_total})

generar_datos_csv()
