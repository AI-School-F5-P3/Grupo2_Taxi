import unittest
import csv
import random
import numpy as np
from datetime import datetime, timedelta
from io import StringIO

# La función original
def generar_datos_csv(file_obj):
    conductores = ['Nathaly', 'Carolina', 'Sergio', 'Angel', 'Jorge'] 
    probabilidades = [0.1, 0.22, 0.15, 0.32, 0.21] 
    inicio = datetime.now() - timedelta(days=170)  # Hace 6 meses

    fieldnames = ['carrera', 'conductor', 'inicio_carrera', 'fin_carrera', 'precio_total']
    writer = csv.DictWriter(file_obj, fieldnames=fieldnames)   
    writer.writeheader()   # Escribe la primera línea del archivo csv. 

    for carrera in range(1, 10001):
        segundos_aleatorios = random.randint(0, 170*24*60*60)  # Segundos aleatorios en los últimos 6 meses
        inicio_carrera = inicio + timedelta(seconds=segundos_aleatorios)
        duracion_viaje = random.randint(300, 2400)  # Duración del viaje en segundos
        fin_carrera = inicio_carrera + timedelta(seconds=duracion_viaje)
        precio_total = round(duracion_viaje * 0.02, 2)  # Precio basado en la duración del viaje
        conductor = np.random.choice(conductores, p=probabilidades)
        # Escribe la línea generada al archivo csv
        writer.writerow({
            'carrera': carrera, 
            'conductor': conductor, 
            'inicio_carrera': inicio_carrera.strftime('%Y-%m-%d %H:%M:%S'), 
            'fin_carrera': fin_carrera.strftime('%Y-%m-%d %H:%M:%S'), 
            'precio_total': precio_total
        })

class TestGenerarDatosCSV(unittest.TestCase):

    def test_generar_datos_csv(self):
        # Usamos StringIO para simular un archivo en memoria
        file_obj = StringIO()
        generar_datos_csv(file_obj)
        file_obj.seek(0)  # Regresamos al inicio del archivo para leerlo

        reader = csv.DictReader(file_obj)
        rows = list(reader)

        # Verificar si se generaron 10000 filas
        self.assertEqual(len(rows), 10000)

        # Verificar si las columnas están presentes
        self.assertEqual(reader.fieldnames, ['carrera', 'conductor', 'inicio_carrera', 'fin_carrera', 'precio_total'])

        # Verificar algunos valores de las filas
        for row in rows:
            self.assertIn(row['conductor'], ['Nathaly', 'Carolina', 'Sergio', 'Angel', 'Jorge'])
            self.assertTrue(datetime.strptime(row['inicio_carrera'], '%Y-%m-%d %H:%M:%S'))
            self.assertTrue(datetime.strptime(row['fin_carrera'], '%Y-%m-%d %H:%M:%S'))
            self.assertTrue(float(row['precio_total']) > 0)

if __name__ == '__main__':
    unittest.main()