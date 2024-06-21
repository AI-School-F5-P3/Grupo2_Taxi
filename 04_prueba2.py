from datetime import datetime
import pytz

class Tarifa:
    precio_parada = 0.02
    precio_movimiento = 0.05
    precio_parada_nocturno = precio_parada * 2
    precio_movimiento_nocturno = precio_movimiento * 2

    def calcular_costo(self, tiempo_transcurrido, hora_inicio, es_movimiento):
        if 22 <= hora_inicio.hour or hora_inicio.hour < 6:
            if es_movimiento:
                return tiempo_transcurrido * self.precio_movimiento_nocturno
            else:
                return tiempo_transcurrido * self.precio_parada_nocturno
        else:
            if es_movimiento:
                return tiempo_transcurrido * self.precio_movimiento
            else:
                return tiempo_transcurrido * self.precio_parada


class Recorrido:
    def __init__(self, inicio_tiempo):
        self.inicio_tiempo = inicio_tiempo
        self.tiempo_transcurrido = 0

    def parada(self, tarifa):
        self.tiempo_transcurrido = (datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
        costo = tarifa.calcular_costo(self.tiempo_transcurrido, self.inicio_tiempo, False)
        print(f"Costo por parada: {costo:.2f}€")
        return costo

    def movimiento(self, tarifa):
        self.tiempo_transcurrido = (datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
        costo = tarifa.calcular_costo(self.tiempo_transcurrido, self.inicio_tiempo, True)
        print(f"Costo por movimiento: {costo:.2f}€")
        return costo

    def finalizar(self, tarifa):
        self.tiempo_transcurrido = (datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
        costo = tarifa.calcular_costo(self.tiempo_transcurrido, self.inicio_tiempo, True)
        print(f"Costo final: {costo:.2f}€")
        return costo


class Carrera:
    def __init__(self, ID, tarifa):
        self.ID = ID
        self.tarifa = tarifa
        self.recorrido = Recorrido(datetime.now(pytz.timezone('Europe/Madrid')))
        self.precio_total = 0
        self.estado = 0

    def parada(self):
        costo = self.recorrido.parada(self.tarifa)
        self.precio_total += costo
        print(f"Total: {self.precio_total:.2f}€")
        self.estado = 0

    def movimiento(self):
        costo = self.recorrido.movimiento(self.tarifa)
        self.precio_total += costo
        print(f"Total: {self.precio_total:.2f}€")
        self.estado = 1

    def finalizar(self):
        costo = self.recorrido.finalizar(self.tarifa)
        self.precio_total += costo
        print(f"Total a pagar: {self.precio_total:.2f}€")
        fecha_final = datetime.now(pytz.timezone('Europe/Madrid'))
        print(f"Carrera finalizada a las {fecha_final.strftime('%Y-%m-%d %H:%M:%S')}.")
    def __str__(self):
        return f"Carrera {self.ID} - Total: {self.precio_total:.2f}€"


nueva_carrera = Carrera(ID=1, tarifa=Tarifa())
print(nueva_carrera)

while True:
    command = input("Presiona enter para iniciar la carrera: ")
    if command == "":
        nueva_carrera.inicio_tiempo = datetime.now(pytz.timezone('Europe/Madrid'))
  # Inicia el tiempo al presionar Enter
        print(f"Carrera iniciada a las {nueva_carrera.inicio_tiempo.strftime('%Y-%m-%d %H:%M:%S')}.")
        break
    else:
        print("Debes pulsar enter para comenzar la carrera.")
        
try:
    while True:
        if nueva_carrera.estado == 0:  # Si el taxi está parado
            command = input("Enter 'M' to move, or 'E' to exit: ")
        elif nueva_carrera.estado == 1:  # Si el taxi está en movimiento
            command = input("Enter 'S' to stop, or 'E' to exit: ")

        if command == "S":
            if nueva_carrera.estado == 1:  # Solo permite parar si está en movimiento
                nueva_carrera.parada()
            else:
                print("El taxi ya está parado. No puedes parar de nuevo.")
        
        elif command == "M":
            if nueva_carrera.estado == 0:  # Solo permite mover si está parado
                nueva_carrera.movimiento()
            else:
                print("El taxi ya está en movimiento. No puedes mover de nuevo.")
        
        elif command == "E":
            nueva_carrera.finalizar()
            break
        
        else:
            print("Comando no válido. Inténtalo de nuevo.")
except KeyboardInterrupt:
    nueva_carrera.finalizar()
