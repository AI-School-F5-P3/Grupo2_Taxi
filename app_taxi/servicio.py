import datetime
import pytz



class Tiempo():
    def __init__(self):
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))

    def reiniciar(self):
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))  # Actualiza el inicio_tiempo al momento actual

    def tiempo_transcurrido(self):
        return (datetime.datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()

    def es_nocturno(self):
        hora = self.inicio_tiempo.hour
        return 22 <= hora or hora < 6
        

class Tarifa():
    def __init__(self, precio_parada=0.02, precio_movimiento=0.05):
        self.precio_parada = precio_parada
        self.precio_movimiento = precio_movimiento
        self.precio_parada_nocturno = precio_parada * 2
        self.precio_movimiento_nocturno = precio_movimiento * 2

    def calcular_costo(self, tiempo_transcurrido, estado, es_nocturno):
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

class Carrera():
    def __init__(self, id):
        self._id = id
        self.tiempo = Tiempo()
        self.tarifa = Tarifa()
        self.estado = 0
        self.precio_total = 0
        self.tiempo_acumulado_parado = 0
        self.tiempo_acumulado_movimiento = 0

    def actualizar_costo(self):
        tiempo_transcurrido = self.tiempo.tiempo_transcurrido()
        es_nocturno = self.tiempo.es_nocturno()
        costo = self.tarifa.calcular_costo(tiempo_transcurrido, self.estado, es_nocturno)
        self.precio_total += costo
        if self.estado == 0:
            self.tiempo_acumulado_parado += tiempo_transcurrido
        elif self.estado == 1:
            self.tiempo_acumulado_movimiento += tiempo_transcurrido
        return costo

    def parada(self):
        if self.estado == 1:  # Si estaba en movimiento, calcular el costo del movimiento
            costo = self.actualizar_costo()
            print(f"Costo por movimiento: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 0  # Cambiar el estado a parado
        self.tiempo.reiniciar()  # Reiniciar el tiempo al momento actual
        print("Taxi parado.")

    def movimiento(self):
        if self.estado == 0:  # Si estaba parado, calcular el costo de la parada
            costo = self.actualizar_costo()
            print(f"Costo por parada: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 1  # Cambiar el estado a movimiento
        self.tiempo.reiniciar()  # Reiniciar el tiempo al momento actual
        print("Taxi en movimiento.")

    def finalizar(self):
        costo = self.actualizar_costo()
        print(f"Precio del último tramo: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 2
        fecha_final = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        print(f"Carrera finalizada a las {fecha_final.strftime('%Y-%m-%d %H:%M:%S')}.")
        print(f"Total a pagar: {self.precio_total:.2f}€")
        input('Presione intro para volver al menú')
        
    def cancelacion(self):
        print(f"Trayecto cancelado")
        self.estado = 3
        fecha_final = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        print(f"Carrera finalizada a las {fecha_final.strftime('%Y-%m-%d %H:%M:%S')}.")
        print(f"Total a pagar: 0€")
        input('Presione intro para volver al menú')
        

# Interfaz de usuario


def iniciar():
    nueva_carrera = Carrera(id=1)
    while True:
        command = input("Presiona enter para iniciar la carrera: ")
        if command == "":
            nueva_carrera.tiempo.reiniciar()  # Inicia el tiempo al presionar Enter
            print(f"Carrera iniciada a las {nueva_carrera.tiempo.inicio_tiempo.strftime('%Y-%m-%d %H:%M:%S')}.")
            break
        else:
            print("Debes pulsar enter para comenzar la carrera.")

    try:
        while True:
            if nueva_carrera.estado == 0:
                command = input("Selecciona 'M' para moverte, 'F' para finalizar la carrera o 'C' para cancelar: ")
            elif nueva_carrera.estado == 1:
                command = input("Enter 'P' para hacer una parada, 'F' para finalizar carrera o 'C' para cancelar: ")

            if command == "P":
                if nueva_carrera.estado == 1:
                    nueva_carrera.parada()
                else:
                    print("El taxi ya está parado. No puedes parar de nuevo.")
            elif command == "M":
                if nueva_carrera.estado == 0:
                    nueva_carrera.movimiento()
                else:
                    print("El taxi ya está en movimiento. No puedes mover de nuevo.")
            elif command == "F":
                nueva_carrera.finalizar()
                break
            elif command == "C":
                nueva_carrera.cancelacion()
                break
            else:
                print("Comando no válido. Inténtalo de nuevo.")
    except KeyboardInterrupt:
        nueva_carrera.finalizar()


