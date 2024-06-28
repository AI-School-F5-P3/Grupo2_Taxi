import datetime  # Módulo para trabajar con fechas y horas
import pytz  # Biblioteca para manejar zonas horarias
import logging  # Módulo para registrar mensajes de depuración y otros eventos en un archivo de registro
import os  # Módulo para interactuar con el sistema operativo, como rutas de archivos
import csv  # Módulo para leer y escribir archivos CSV (valores separados por comas)
import generar_informes  # Módulo específico del proyecto para generar informes (no estándar, definido por el usuario)
import shared  # Módulo compartido del proyecto para variables y configuraciones comunes (no estándar, definido por el usuario)

fichero_contador = 'contador_carreras.txt'
fichero_carreras = 'carreras.csv'

# Clase que maneja el tiempo
class Tiempo(): 
    def __init__(self):
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid')) # (pytz.timezone('Europe/Madrid') fija la zona horaria de la península

    def reiniciar(self): 
        # Actualiza inicio_tiempo al momento actual
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))  
        logging.debug('inicio tiempo actualizado')
    def tiempo_transcurrido(self): 
        # Resta el momento actual - inicio timepo
        return (datetime.datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()

    def es_nocturno(self): 
        # Si el servicio se efectúa entre las 22h y las 6h, se cobra la tarifa nocturna.
        hora = self.inicio_tiempo.hour
        return 22 <= hora or hora < 6
        

class Tarifa():
    def __init__(self):
        self.precio_parada = shared.tarifa_parada
        self.precio_movimiento = shared.tarifa_movimiento
        self.precio_parada_nocturno = shared.tarifa_parada_nocturna
        self.precio_movimiento_nocturno = shared.tarifa_movimiento_nocturna
    def calcular_costo(self, tiempo_transcurrido, estado, es_nocturno):
        # Calcula el costo basado en el tiempo transcurrido, el estado (parado o movimiento), y si es horario nocturno
        if estado == 0:  # parado
            if es_nocturno:
                return tiempo_transcurrido * self.precio_parada_nocturno
            else:
                return tiempo_transcurrido * self.precio_parada
        elif estado == 1:  # movimiento
            if es_nocturno:
                return tiempo_transcurrido * self.precio_movimiento_nocturno
            else:
                return tiempo_transcurrido * self.precio_movimiento
        return 0
    
# Método de cambio de tarifa
def cambiar_tarifa():
    # Cambio de tarifa en parada
    while True:
        nueva_tarifa_parada = input('Introduzca nueva tarifa diurna de parada (la nocturna duplica este valor) : ')
        try:
            shared.tarifa_parada = float(nueva_tarifa_parada) # Hay que transformar nueva_tarifa_parada a float
            shared.tarifa_parada_nocturna = float(nueva_tarifa_parada) * 2
            break
        except ValueError:
            logging.warning('Método de cambio de tarifa: El valor ingresado no es del tipo float')
            print('Entrada no válida. Inténtelo nuevamente')

    # Cambio de tarifa en movimiento        
    while True:
        nueva_tarifa_movimiento = input('Introduzca nueva tarifa diurna en movimiento (la nocturna duplica este valor) : ')
        try:
            shared.tarifa_movimiento = float(nueva_tarifa_movimiento) # Hay que transformar nueva_tarifa_movimiento a float
            shared.tarifa_movimiento_nocturna = float(nueva_tarifa_movimiento) * 2
            break
        except ValueError:
            logging.warning('Método de cambio de tarifa: El valor ingresado no es del tipo float')
            print('Entrada no válida. Inténtelo nuevamente')
# Fin de método de cambio de tarifa

#Clase que representa una carrera
class Carrera():
    
    def __init__(self, id):
        self.id = id
        self.tiempo = Tiempo()
        self.tarifa = Tarifa()
        self.estado = 0  # 0: parado, 1: en movimiento, 2: finalizado, 3: cancelado
        self.precio_total = 0
        self.tiempo_acumulado_parado = 0 # Se irán sumando valores mientras avance la carrera
        self.tiempo_acumulado_movimiento = 0 # Se irán sumando valores mientras avance la carrera
        self.inicio_carrera_info = datetime.datetime.now(pytz.timezone('Europe/Madrid')) # Solo se usa para generar_informes
        self.fin_carrera_info = datetime.datetime.now(pytz.timezone('Europe/Madrid')) # Solo se usa para generar_informes


    def actualizar_costo(self):
        #Actualiza el costo acumulado tras cada cambio de estado
        tiempo_transcurrido = self.tiempo.tiempo_transcurrido()
        es_nocturno = self.tiempo.es_nocturno()
        costo = self.tarifa.calcular_costo(tiempo_transcurrido, self.estado, es_nocturno)
        self.precio_total += costo
        if self.estado == 0: # Si venía de estar parado
            self.tiempo_acumulado_parado += tiempo_transcurrido
        elif self.estado == 1: # Si venía de estar en movimiento
            self.tiempo_acumulado_movimiento += tiempo_transcurrido
        return costo

    def parada(self):
        if self.estado == 1:  # Calcula el costo del movimiento
            costo = self.actualizar_costo()
            print(f"Costo por movimiento: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 0  # Cambiar el estado a parado
        self.tiempo.reiniciar()  # Reiniciar el tiempo al momento actual
        print("Taxi parado.")
        logging.info('el taxi se para')
    
    def movimiento(self):
        if self.estado == 0:  # Calcula el costo de la parada
            costo = self.actualizar_costo()
            print(f"Costo por parada: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 1  # Cambiar el estado a movimiento
        self.tiempo.reiniciar()  # Reiniciar el tiempo al momento actual
        print("Taxi en movimiento.")
        logging.info('taxi en movimiento')

    def finalizar(self):
        # Finaliza la carrera y muestra el costo total
        costo = self.actualizar_costo()
        print(f"Precio del último tramo: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 2 # Finalizar la carrera
        fecha_final = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        self.fin_carrera_info = fecha_final
        print(f"Carrera {self.id} finalizada a las {fecha_final.strftime('%H:%M horas del día %d-%m-%Y')}.")
        logging.info('carrera finalizada')
        print(f"Total a pagar: {self.precio_total:.2f}€")
        self.generar_informe_carrera(fichero_carreras)
        input('Presione intro para volver al menú')
        
    def cancelacion(self):
        #Cancelar la carrera e imprimir coste 0€
        print(f"Trayecto cancelado")
        self.estado = 3
        fecha_final = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        self.fin_carrera_info = fecha_final
        print(f"Carrera {self.id} finalizada a las {fecha_final.strftime('%H:%M horas del día %d-%m-%Y')}.")
        self.precio_total = 0
        print(f"Total a pagar: 0€")
        self.generar_informe_carrera(fichero_carreras)
        logging.debug('carrera cancelada')
        input('Presione intro para volver al menú')

    def generar_informe_carrera(self,nombre_fichero):
        # Genera un informe de la carrera y lo guarda en un archivo CSV
        ubicacion = os.path.join(os.path.dirname(__file__),nombre_fichero)
        with open(ubicacion, 'a', newline = '') as file:
            csv_writer = csv.writer(file)
            csv_data = [self.id, shared.usuario_activo, self.inicio_carrera_info.strftime('%Y-%m-%d %H:%M:%S'), self.fin_carrera_info.strftime('%Y-%m-%d %H:%M:%S'), round(self.precio_total,2)]
            csv_writer.writerow(csv_data)
        return


# Interfaz de usuario


def iniciar():
    # Crea una nueva instancia de Carrera con un número de carrera generado
    nueva_carrera = Carrera(generar_informes.generar_numero_carrera(fichero_contador))
    
    while True: # Bucle para esperar a que el usuario presione Enter para iniciar la carrera
        command = input("Presiona enter para iniciar la carrera: ")
        if command == "":
            nueva_carrera.tiempo.reiniciar()  # Inicia el tiempo al presionar Enter
            print(f"Carrera iniciada a las {nueva_carrera.tiempo.inicio_tiempo.strftime('%H:%M horas del día %d-%m-%Y')}.")
            logging.debug('carrera iniciada')
            break # Sale del bucle una vez que la carrera ha comenzado
        else:
            print("Debes pulsar enter para comenzar la carrera.")

    try:
        while True:
            # Bucle principal para manejar los comandos del usuario durante la carrera
            if nueva_carrera.estado == 0:
                # Si el taxi está parado, muestra las opciones disponibles
                command = input("Selecciona 'M' para moverte, 'F' para finalizar la carrera o 'C' para cancelar: ")
            elif nueva_carrera.estado == 1:
                # Si el taxi está en movimiento, muestra las opciones disponibles
                command = input("Enter 'P' para hacer una parada, 'F' para finalizar carrera o 'C' para cancelar: ")
            if command.upper() == "P":
                # Si el taxi está en movimiento, realiza una parada
                if nueva_carrera.estado == 1:
                    nueva_carrera.parada()
                else:
                    print("El taxi ya está parado. No puedes parar de nuevo.")
            elif command.upper() == "M":
                # Si el taxi está parado, comienza a moverse
                if nueva_carrera.estado == 0:
                    nueva_carrera.movimiento()
                else:
                    print("El taxi ya está en movimiento. No puedes mover de nuevo.")
            elif command.upper() == "F":
                # Finaliza la carrera
                nueva_carrera.finalizar()
                break # Sale del bucle una vez que la carrera ha finalizado
            elif command.upper() == "C":
                # Cancela la carrera
                nueva_carrera.cancelacion()
                break # Sale del bucle si se cancela la carrera
            else:
                print("Comando no válido. Inténtalo de nuevo.")
    except KeyboardInterrupt:
        # Maneja la interrupción del programa mediante Ctrl+C
        logging.warning('carrera interrumpida, se finaliza carrera')
        nueva_carrera.finalizar()


