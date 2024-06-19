import datetime

class Carrera():
    precio_parada = 0.02
    precio_movimiento = 0.05  # Corrigiendo la coma
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
        self.inicio_tiempo = datetime.datetime.now()
        self.precio_total = 0

    def parada(self):
        if self.estado == 1:  # Si estaba en movimiento, calcular el costo del movimiento
            tiempo_transcurrido = (datetime.datetime.now() - self.inicio_tiempo).total_seconds()
            # Verificar si se inició el viaje en horario nocturno (de 22:00 a 06:00)
            if 22 <= self.inicio_tiempo.hour < 6:
                costo = tiempo_transcurrido * self.precio_movimiento * 2
            else:
                costo = tiempo_transcurrido * self.precio_movimiento
        
            self.precio_total += costo
            self.tiempo_acumulado_movimiento += tiempo_transcurrido
            print(f"Costo por movimiento: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")

        self.estado = 0  # Cambiar el estado a parado
        self.inicio_tiempo = datetime.datetime.now()
        print("Taxi parado.")

    def movimiento(self):
        if self.estado == 0:  # Si estaba parado, calcular el costo de la parada
            tiempo_transcurrido = (datetime.datetime.now() - self.inicio_tiempo).total_seconds()
            # Verificar si se inició el viaje en horario nocturno (de 22:00 a 06:00)
            if 22 <= self.inicio_tiempo.hour < 6:
                costo = tiempo_transcurrido * self.precio_parada * 2
            else:
                costo = tiempo_transcurrido * self.precio_parada
        
            self.precio_total += costo
            self.tiempo_acumulado_parado += tiempo_transcurrido
            print(f"Costo por parada: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 1  # Cambiar el estado a movimiento
        self.inicio_tiempo = datetime.datetime.now()
        print("Taxi en movimiento.")

    def finalizar(self):
        #if self.estado != 2:
        #tiempo_transcurrido = (datetime.datetime.now() - self.inicio_tiempo_estado).total_seconds()
        if self.estado == 0:  # Si estaba parado, calcular el costo de la parada
            tiempo_transcurrido = (datetime.datetime.now() - self.inicio_tiempo).total_seconds()
            if 22 <= self.inicio_tiempo.hour < 6:
                costo = tiempo_transcurrido * self.precio_parada * 2
            else:
                costo = tiempo_transcurrido * self.parada
            self.precio_total += costo
            self.tiempo_acumulado_parado += tiempo_transcurrido

        if self.estado == 1:  # Si estaba en movimiento, calcular el costo del movimiento
            tiempo_transcurrido = (datetime.datetime.now() - self.inicio_tiempo).total_seconds()
            if 22 <= self.inicio_tiempo.hour < 6:
                costo = tiempo_transcurrido * self.precio_movimiento * 2
            else:
                costo = tiempo_transcurrido * self.precio_movimiento
            self.precio_total += costo
            self.tiempo_acumulado_movimiento += tiempo_transcurrido
        
        self.precio_total += costo
        print(f"Costo final: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
    
        self.estado = 2
        fecha_final = datetime.datetime.now()
        print(f"Carrera finalizada a las {fecha_final.strftime('%Y-%m-%d %H:%M:%S')}.")
        print(f"Total a pagar: {self.precio_total:.2f}€")


nueva_carrera = Carrera(tiempo=10, ID=1, estado=0)

input("Presiona enter para iniciar la carrera: ")
try:
    while True:
        command = (input("Enter 'S' to start/stop, 'M' to move, or 'E' to exit: "))
        if command == "S":

            # Crear una instancia de la clase Carrera
              # Por ejemplo, con tiempo 10 segundos, ID 1 (por ejemplo) y estado 1 (en movimiento)

            # Llamar al método "parada" en la instancia de la clase Carrera
            nueva_carrera.parada()
        elif command == "M":
            nueva_carrera.movimiento()
        elif command == "E":
            nueva_carrera.finalizar()
            break
except KeyboardInterrupt:
    nueva_carrera.finalizar()
