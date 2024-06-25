
import os, csv, datetime, pytz

fichero_contador = 'contador_carreras.txt'
fichero_carreras = 'carreras.csv'

class Carrera():
    
    def __init__(self, id):
        self._id = id
        #self.tiempo = Tiempo()
        #self.tarifa = Tarifa()
        self.estado = 0
        self.precio_total = 0
        self.tiempo_acumulado_parado = 0
        self.tiempo_acumulado_movimiento = 0
        self.fecha_inicial = datetime.datetime.now(pytz.timezone('Europe/Madrid')) #solo se usa para generar_informes

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


def generar_informe_carrera(nombre_fichero):
        ubicacion = os.path.join(os.path.dirname(__file__),nombre_fichero)
        with open(ubicacion, 'a', newline = '') as file:
            csv_writer = csv.writer(file)
            csv_data = [nueva_carrera._id, nueva_carrera.fecha_inicial, nueva_carrera.fecha_inicial, 10.34]
            #csv_data = [self._id, self.fecha_inicial, self.fecha_final, self.precio_total]
            csv_writer.writerow(csv_data)
        return

nueva_carrera = Carrera(generar_numero_carrera(fichero_contador))

generar_informe_carrera(fichero_carreras)