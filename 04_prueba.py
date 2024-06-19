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
            costo = tiempo_transcurrido * self.precio_parada
            self.precio_total += costo
            self.tiempo_acumulado_parado += tiempo_transcurrido
            print(f"Costo por parada: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 1  # Cambiar el estado a movimiento
        self.inicio_tiempo = datetime.datetime.now()
        print("Taxi en movimiento.")

    def finalizar(self):
        if self.estado == 2:
            self.precio_final = (self.tiempo_acumulado_parado*self.precio_parada)+(self.tiempo_acumulado_movimiento*self.precio_movimiento)
            print(F"Has finalizado tu viaje. El coste total es de {self.precio_total}")



#Un bucle ??
#carrera = Carrera(10,1,0)
#parar=carrera.parada()
nueva_carrera = Carrera(tiempo=10, ID=1, estado=1)
#arrancar=carrera.movimiento()
#fin=carrera.finalizar()
input("Presiona enter para iniciar la carrera: ")
try:
    while True:
        command = (input("Enter 'S' to start/stopp, 'M' to move, or 'E' to exit: "))
        if command == "I":

            # Crear una instancia de la clase Carrera
              # Por ejemplo, con tiempo 10 segundos, ID 1 (por ejemplo) y estado 1 (en movimiento)

            # Llamar al método "parada" en la instancia de la clase Carrera
            nueva_carrera.parada()
        elif command == "S":
            nueva_carrera.movimiento()
        elif command == "E":
            nueva_carrera.finalizar()
            break
except KeyboardInterrupt:
    nueva_carrera.finalizar()

# Print the total fare
print("Tarifa Total: {:.2f} Euros".format(nueva_carrera.precio_total))
