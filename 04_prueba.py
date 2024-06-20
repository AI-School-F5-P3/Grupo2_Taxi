import datetime
import pytz

class Carrera():
    precio_parada = 0.02
    precio_movimiento = 0.05 
    precio_parada_nocturno = precio_parada * 2
    precio_movimiento_nocturno = precio_movimiento * 2
    fecha_inicio = 0
    fecha_final =  0
    ID = 0
    tiempo_acumulado_parado = 0
    tiempo_acumulado_movimiento = 0
    tipo_estado = {0: "parado", 1: "movimiento", 2: "otro"}
    estado = 0
    tiempo_total = 0

    def __init__(self, tiempo, ID, estado):
        self._ID = ID
        self.tiempo = tiempo
        self.estado = estado
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        self.precio_total = 0

    def parada(self):
        if self.estado == 1:  # Si estaba en movimiento, calcular el costo del movimiento
            tiempo_transcurrido = (datetime.datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
            # Verificar si se inició el viaje en horario nocturno (de 22:00 a 06:00)
            if 22 <= self.inicio_tiempo.hour or self.inicio_tiempo.hour < 6:
                costo = tiempo_transcurrido * self.precio_movimiento_nocturno
            else:
                costo = tiempo_transcurrido * self.precio_movimiento

            self.precio_total += costo
            self.tiempo_acumulado_movimiento += tiempo_transcurrido
            print(f"Costo por movimiento: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")

        self.estado = 0  # Cambiar el estado a parado
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        print("Taxi parado.")

    def movimiento(self):
        if self.estado == 0:  # Si estaba parado, calcular el costo de la parada
            tiempo_transcurrido = (datetime.datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
            # Verificar si se inició el viaje en horario nocturno (de 22:00 a 06:00)
            if 22 <= self.inicio_tiempo.hour or self.inicio_tiempo.hour < 6:
                costo = tiempo_transcurrido * self.precio_parada_nocturno
            else:
                costo = tiempo_transcurrido * self.precio_parada

            self.precio_total += costo
            self.tiempo_acumulado_parado += tiempo_transcurrido
            print(f"Costo por parada: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 1  # Cambiar el estado a movimiento
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        print("Taxi en movimiento.")

    def finalizar(self):
        tiempo_transcurrido = (datetime.datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
    
        if 22 <= self.inicio_tiempo.hour or self.inicio_tiempo.hour < 6:
            if self.estado == 0:
                costo = tiempo_transcurrido * self.precio_parada_nocturno
            else:
                costo = tiempo_transcurrido * self.precio_movimiento_nocturno
        else:
            if self.estado == 0:
                costo = tiempo_transcurrido * self.precio_parada
            else:
                costo = tiempo_transcurrido * self.precio_movimiento
    
        self.precio_total += costo

        print(f"Costo final: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")

        self.estado = 2
        fecha_final = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        print(f"Carrera finalizada a las {fecha_final.strftime('%Y-%m-%d %H:%M:%S')}.")
        print(f"Total a pagar: {self.precio_total:.2f}€")


nueva_carrera = Carrera(tiempo=10, ID=1, estado=0)

while True:
    command = input("Presiona enter para iniciar la carrera: ")
    if command == "":
        nueva_carrera.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))  # Inicia el tiempo al presionar Enter
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
